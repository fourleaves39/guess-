import random
import xml.etree.ElementTree as ET

def guess_the_number(x1, x2, max_attempts):
    target_number = random.randint(x1, x2)
    
    print(f"猜數字遊戲開始！目標數字在 {x1} 到 {x2} 之間。")

    attempts = 0

    while attempts < max_attempts:
        guess = int(input("請猜一個數字："))

        if guess == target_number:
            print(f"恭喜你，猜對了！目標數字是 {target_number}。")
            break
        elif guess < target_number:
            print("太低了，請再試一次。")
        else:
            print("太高了，請再試一次。")

        attempts += 1

    if attempts == max_attempts:
        print(f"很抱歉，你已經猜了 {max_attempts} 次，遊戲結束。正確答案是 {target_number}。")

    return target_number, attempts

def save_to_file(x1, x2, n, result):
    file = open("result.txt", "w", encoding="utf-8")
    file.write(f"遊戲設定:\n")
    file.write(f"目標數字範圍: {x1} 到 {x2}\n")
    file.write(f"最大猜測次數: {n}\n\n")
    file.write("遊戲結果:\n")
    file.write(f"玩家{'成功' if result[1] < n else '失敗'}猜對目標數字！\n")
    file.write(f"猜測次數: {result[1]}\n")
    file.write(f"目標數字是: {result[0]}\n")
    file.close()

if __name__ == "__main__":
    # 讀取 XML 設定
    tree = ET.parse("setting.xml")
    root = tree.getroot()

    x1 = int(root.find("x1").text)
    x2 = int(root.find("x2").text)
    n = int(root.find("n").text)

    # 開始遊戲
    result = guess_the_number(x1, x2, n)

    # 儲存遊戲結果到記事本
    save_to_file(x1, x2, n, result)
