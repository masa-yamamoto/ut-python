#argsnum.py
import sys
num = len(sys.argv) - 1 # sys.argvの先頭は実行するファイルの名前であって引数ではないので、1減らす
if num <= 3:
    print(num)
else:
    print("too many")