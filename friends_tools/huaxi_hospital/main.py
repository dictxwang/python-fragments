# -*- coding: utf8 -*-
import requests
import json
import concurrent.futures
import time
import random


api_host = "mcpwxp.motherchildren.com"
api_prefix = f"https://{api_host}"
access_token = "{your access token. get it by web proxy like Charles or Fiddler}"

def make_req_headers():
    return {
        "Host": api_host,
        "accessToken": access_token,
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a31) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wx38285c6799dac2d1/104/page-frame.html"
    }


def sel_doctor_list(dept_id, page_no=1, page_size=50):
    body = {
        "appCode": "HXFYAPP",
        "channelCode": "PATIENT_WECHAT_APPLET",
        "pageNum": page_no,
        "pageSize": page_size,
        "query": {
            "channelCode": "PATIENT_WECHAT_APPLET",
            "organCode": "HXD2",
            "interRangfaceIndex": "",
            "deptId": f"{dept_id}",
            "isHaveNo": "false",
            "selectionTypeId": "",
            "bizIndex": "",
            "scheduleDate": "",
            "keyWord": "",
            "keyWordType": "doctorName"
        },
        "channel": "MOBILE"
    }
    url = f"{api_prefix}/cloud/appointment/publicClient/selDoctorListPaging"
    resp = requests.post(url, headers=make_req_headers(), json=body)
    resp.encoding = "utf8"
    return resp.text


def sel_doctor_schedule(doctor_id,
                        organ_code="platform",
                        app_code="HXFYAPP",
                        channel_code="PATIENT_WECHAT_APPLET"):
    body  = {
        "organCode": organ_code,
        "appCode": app_code,
        "channelCode": channel_code,
        "doctorId": doctor_id
    }
    url = f"{api_prefix}/cloud/appointment/publicClient/selDoctorSchedule"

    print(f"[step] start crawl doctor {doctor_id} schedule")
    resp = requests.post(url, headers=make_req_headers(), json=body)
    resp.encoding = "utf8"
    return resp.text


def parse_doctor_schedule(doctor_id, doctor_name, schedule_content, only_has_no=True, skip_dates=None, max_cost=120.00, organ_codes=None):
    schedule_content = remove_invalid_json_char(schedule_content)
    obj = json.loads(schedule_content)
    result = []
    if obj["code"] != "1":
        print(f"[error] parse doctor {doctor_id} schedule", obj)
    if obj["code"] == "1" and "data" in obj and "scheduleRespVo" in obj["data"] and "scheduleRespVos" in obj["data"]["scheduleRespVo"]:
        for schedule in obj["data"]["scheduleRespVo"]["scheduleRespVos"]:
            available_count = int(schedule["availableCount"])
            cost = float(schedule["cost"].replace("￥", ""))
            schedule_date = schedule["scheduleDate"]
            organ_code = schedule["organCode"]
            if only_has_no and available_count <= 0:
                continue
            if skip_dates and schedule_date in skip_dates:
                continue
            if cost > max_cost:
                continue
            if organ_codes and organ_code not in organ_codes:
                continue
            result.append({
                "doctorId": str(doctor_id),
                "doctorName": str(doctor_name),
                "sysScheduleId": str(schedule["sysScheduleId"]),
                "organCode": schedule["organCode"],
                "scheduleDate": schedule["scheduleDate"],
                "timeRange": schedule["timeRange"],
                "cost": schedule["cost"],
                "statusName": schedule["statusName"],
                "availableCount": schedule["availableCount"]
            })
    return result


def remove_invalid_json_char(text):
    text = text.replace("\t", "")
    return text

def format_json_and_save(content, save_path):
    content = remove_invalid_json_char(content)
    obj = json.loads(content)
    format_json = json.dumps(obj, ensure_ascii=False, indent=4)
    with open(save_path, mode="w", encoding="utf8") as fp:
        fp.write(format_json)
        fp.flush()


def format_json_and_print(obj, banner):
    format_json = json.dumps(obj, ensure_ascii=False, indent=4)
    print("{} start print {} {}".format("*" * 20, banner, "*" * 20))
    print(format_json)
    print("{} end print {} {}".format("*" * 20, banner, "*" * 20))

def parse_for_doctors_info(save_path):
    with open(save_path, mode="r", encoding="utf8") as fp:
        obj = json.load(fp)
    content = obj["data"]["content"]

    result = {}  # regTitleName: [doctors]
    for info in content:
        doctor = {
            "doctorId": str(info["doctorId"]),
            "doctorName": str(info["doctorName"]),
            "regTitelName": str(info["regTitelName"]),
            "isCanAppointment": str(info["isCanAppointment"])
        }
        title = str(info["regTitelName"])
        if title in result:
            result[title].append(doctor)
        else:
            result[title] = [doctor]
    return result


def filter_appointment_doctors(doctors, appointment_filters):

    result = []
    for appointment_filter in appointment_filters:
        title = appointment_filter["title"]
        if title not in doctors:
            print(f"[warning] not found doctor with title {title}")
            continue

        include_names = appointment_filter["include_names"]
        exclude_names = appointment_filter["exclude_names"]
        for doctor in doctors[title]:
            if len(include_names) > 0 and doctor["doctorName"] not in include_names:
                continue
            if len(exclude_names) > 0 and doctor["doctorName"] in exclude_names:
                continue
            result.append(doctor)

    return result


def find_doctor_available_schedule(doctor_id="", doctor_name="", skip_dates=None, max_cost=120.00, organ_codes=["HXD2"]):

    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)
    schedule_content = sel_doctor_schedule(doctor_id)
    available_schedule = parse_doctor_schedule(doctor_id,
                                               doctor_name,
                                               schedule_content,
                                               skip_dates=skip_dates,
                                               max_cost=max_cost,
                                               organ_codes=organ_codes)
    return available_schedule


def get_all_available_schedules(appointment_doctors, skip_dates=None, max_cost=120.00, organ_codes=["HXD2"]):

    all_available_schedules = []
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for doctor in appointment_doctors:
            future = executor.submit(find_doctor_available_schedule,
                                     doctor["doctorId"], doctor["doctorName"],
                                     skip_dates, max_cost, organ_codes)
            futures.append(future)

        # for schedule in future.result():
        #     all_available_schedules.append(schedule)
        for future in concurrent.futures.as_completed(futures):
            for schedule in future.result():
                all_available_schedules.append(schedule)
    return sorted(all_available_schedules, key=lambda s: s["availableCount"], reverse=True)


if __name__ == '__main__':

    need_crawl_doctors = False
    dept_id = 117
    file_path = f"data/all_doctors_at_dept_{dept_id}.json"
    skip_schedule_dates = []  # 需要跳过的预约日期
    max_cost_per_schedule = 120.00  # 单次挂号费上限
    organ_codes = ["HXD2"]  # 院区代号 ['MSFYBJ', 'HXD2']
    appointment_filters = [
        {
            "title": '一级专家',  # all['四级专家', '三级专家', '专科医师', '二级专家', '一级专家']
            "include_names": [],
            "exclude_names": [],
        },
        {
            "title": '二级专家',
            "include_names": [],
            "exclude_names": [],
        },
        {
            "title": '三级专家',
            "include_names": [],
            "exclude_names": [],
        },
        {
            "title": '四级专家',
            "include_names": [],
            "exclude_names": [],
        }
        # ********** FOR TEST **********
        # {
        #     "title": "专科医师",
        #     "include_names": ['李克敏', '张建军'],
        #     "exclude_names": [],
        # }
    ]
    if need_crawl_doctors:
        doctors_info = sel_doctor_list(dept_id)
        print(f"[step] select doctor list for detp {dept_id}")

        format_json_and_save(doctors_info, save_path=file_path)
        print(f"[step] save doctor info as json for detp {dept_id}")

    doctors = parse_for_doctors_info(file_path)
    print(f"[step] parse doctors info, all title {doctors.keys()}")

    appointment_doctors = filter_appointment_doctors(doctors, appointment_filters)
    print(f"[step] filter {len(appointment_doctors)} doctors for appointment")
    # format_json_and_print(appointment_doctors, "Appointment Doctors")

    all_available_schedules = get_all_available_schedules(appointment_doctors,
                                                          skip_dates=skip_schedule_dates,
                                                          max_cost=max_cost_per_schedule,
                                                          organ_codes=organ_codes)
    print(f"[step] found {len(all_available_schedules)} doctor available schedules")
    if len(all_available_schedules) > 0:
        format_json_and_print(all_available_schedules, "Available Schedules")
