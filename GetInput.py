import requests
requests.packages.urllib3.disable_warnings()

class GetInput():

    def __init__(self):
        self.headers = '53616c7465645f5ff6c06a7610c7c7481d332d3a7b9ef384508acd8e74a0d4bd01f017ffdf76da9394bd97c543272c25'
    
    def get_input(self, day):
        headers = {'session': self.headers}
        session = requests.Session()
        ins = session.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=headers, verify=False)
        with open(f'day{day}.txt', 'w', newline='') as file:
            file.write(ins.text)