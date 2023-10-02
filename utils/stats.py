from datetime import datetime
import os

def count_files(directory):
    total_count = 0
    subdirs_info = ""
    entries = sorted(os.scandir(directory), key=lambda entry: entry.name)
    for entry in entries:
        if entry.is_file() and os.path.splitext(entry.name)[1] == '.js':
            total_count += 1
        elif entry.is_dir():
            subdir_count, subdir_info = count_files(entry.path)
            total_count += subdir_count
            subdirs_info += f"    - [{entry.name}]: {subdir_count}개 해결\n" + subdir_info
    return total_count, subdirs_info

def update_readme(file_counts):
    info = ""
    for directory, (count, subdirs_info) in file_counts.items():
        info += f"- [{directory}]: {count}개 해결\n" + subdirs_info

    total_count = sum(count for count, _ in file_counts.values())

    total_info = f"### 누적 기록\n#### 총 합계: {total_count}\n" + info

    readme = f"""# Python CodingTest
### _파이썬 코딩테스트_
# 개요
>온라인 저지(Online Judge)에서 [Python]로 해결 중인 코딩 문제를 업로드 하는 리포지토리.
# 상세
- 원래는 자바스크립트에서 하려고 했는데 파이썬으로 변경함.
  - 자바스크립트는 input 측면에서 코딩 테스트에서 불편한 점이 많았음.
  - 가장 큰 이유로 일부 기업은 자바스크립트를 코딩 테스트 언어로 지원 안 하기도 했음.
  - 불가피한 측면이 있다고 판단하여 변경.
{total_info}
### 사용 환경
| 종류 | 목록 |
| ------ | ------ |
| 사용 언어 | Python |
| 개발 도구 | Visual Studio Code |
| OS 환경 | Windows 10 |

   [Python]: <https://www.python.org/>
   [./Baekjoon]: <https://www.acmicpc.net/>
   [./Programmers]: <https://programmers.co.kr/>
"""

    with open("./README.MD", 'w', encoding='utf-8') as f:
        f.write(readme)

if __name__ == "__main__":
    directories = ["./Programmers", "./Baekjoon"]
    file_counts = {directory: count_files(directory) for directory in directories}
    update_readme(file_counts)
