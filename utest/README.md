### pytest简介
python主流的测试框架有：pytest > nose > unittest(python自带)，其中pytest在入门便捷性、生态优势和通用性三个方面都最优的。
### pytest安装
pip install pytest
### pytest的插件体系
pytest-html # 生成html报表

pytest-cov  # 计算测试的代码覆盖率

pytest-asyncio  # 异步测试框架

pytest-sugar    # 添加测试进度条

pytest-parallel # 并行测试框架

pytest-ordering # 改变pytest默认的执行顺序
### pytest常用命令
#### 运行测试用例
pytest tools.py  # 运行所有用例（递归查找所有test开头或结尾的用例）

pytest tools.py::test_success  # 运行指定用例（需要test开头）

pytest -k xx tools.py  # 运行xx模糊匹配的用例

pytest -m finished tools.py  # 运行加上了@pytest.mark.finished 注解的用例，finished是自定义的标记
#### 生成测试报告
pytest --html=../pytest_report/test_report.html test_tools.py  # 生成html报告

pytest --html=../pytest_report/test_report.html --cov --cov-report=html test_tools.py  # 同时生成html包含和覆盖率报告

### python虚拟环境
#### 创建虚拟环境
python3 -m venv xvenv   # 创建名为xvenv的虚拟环境，版本是python3命令对应的版本
#### 使用虚拟环境
source xvenv/bin/activate
#### 在虚拟环境安装pipy包
pip install pytest  # 这里pip不需要版本号
#### 在虚拟环境运行脚本
python my.py    # 同样这里python不需要版本号
#### 退出虚拟环境
deactive
