import csv
import tkinter
import datetime as dt
from datetime import datetime
import re

#CSVファイルの読み込み
member = []

with open('Book1.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        member.append(line)

WAREKI_START = {
   '令和': datetime(2019, 5, 1),
   '平成': datetime(1989, 1, 8),
   '昭和': datetime(1926, 12, 25),
   '大正': datetime(1912, 7, 30),
   '明治': datetime(1868, 1, 1)
}


def convert_to_wareki(y, m, d):
    """西暦の年月日を和暦の年に変換する."""
    try:
        y_m_d = datetime(y, m, d)
        if WAREKI_START['令和'] <= y_m_d:
            reiwa_year = WAREKI_START['令和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '令和'
        elif WAREKI_START['平成'] <= y_m_d:
            reiwa_year = WAREKI_START['平成'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '平成'
        elif WAREKI_START['昭和'] <= y_m_d:
            reiwa_year = WAREKI_START['昭和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '昭和'
        elif WAREKI_START['大正'] <= y_m_d:
            reiwa_year = WAREKI_START['大正'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '大正'
        elif WAREKI_START['明治'] <= y_m_d:
            reiwa_year = WAREKI_START['明治'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '明治'

        if year == 1:
            year = '元'
       
        return era_str + str(year) + '年' + str(m) + '月' + str(d) + '日生'
    except ValueError as e:
        raise e

def age(year, month, day):
    ToDay = dt.date.today()
    birthday = dt.date(year, month, day)
    return (int(ToDay.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

def search_family(fam):
    if "高" in fam:
        numbers = re.sub(r'[^0-9]', '', fam)
        return "高齢者" + str(numbers) + "名家族"
    
    elif "独居" in fam:
        return fam
    
    else:
        return str(fam) + "名家族"
    
#クリックイベントの作成
def btn_click():
    name = txt.get()
    if name == "":
        pass
    else:
        for i in range(len(member)):
            if name in member[i][0]:
                txtp1.insert(0, member[i][6])
                txtp2.insert(0, member[i][7])
                txtp3.insert(0, member[i][8])
                txtp4.insert(0, member[i][9])
                txtg.insert(0, member[i][10])
                txtb = "西暦" + member[i][1] + "年" + member[i][2] + "月" + member[i][3] + "日生"
                txtbir.insert(0, txtb)
                txtbj = convert_to_wareki(int(member[i][1]), int(member[i][2]), int(member[i][3]))
                txtbirj.insert(0, txtbj)
                txta.insert(0, age(int(member[i][1]), int(member[i][2]), int(member[i][3])))
                txtp.insert(0, member[i][4])
                txtf.insert(0, search_family(member[i][5]))

def btn_click_delete():
    txt.delete(0, tkinter.END)
    txtp1.delete(0, tkinter.END)
    txtp2.delete(0, tkinter.END)
    txtp3.delete(0, tkinter.END)
    txtp4.delete(0, tkinter.END)
    txtg.delete(0, tkinter.END)
    txtbir.delete(0, tkinter.END)
    txtbirj.delete(0, tkinter.END)
    txta.delete(0, tkinter.END)
    txtp.delete(0, tkinter.END)
    txtf.delete(0, tkinter.END)


#GUIの作成
root = tkinter.Tk()
root.geometry('1800x900')
root.title('高年調査')
labeltitle = tkinter.Label(text='検索したい方の名前を入力してください', font=("Times", 30))
labeltitle.place(x=200, y=50)
label = tkinter.Label(text='名前', font=("Times", 30))
label.place(x=200, y=200)
labelbir = tkinter.Label(text='生年月日', font=("Times", 30))
labelbir.place(x=200, y=250)
labela = tkinter.Label(text='歳', font=("Times", 30))
labela.place(x=1300, y=250)
labelg = tkinter.Label(text='班', font=("Times", 30))
labelg.place(x=300, y=150)
labelp = tkinter.Label(text='連絡先', font=("Times", 30))
labelp.place(x=300, y=300)
labelf = tkinter.Label(text='家族構成', font=("Times", 30))
labelf.place(x=300, y=350)
labelpp1 = tkinter.Label(text='緊急連絡先１', font=("Times", 30))
labelpp1.place(x=300, y=400)
labelp1 = tkinter.Label(text='緊急連絡先１の電話番号', font=('Times', 30))
labelp1.place(x=300, y=450)
labelpp2 = tkinter.Label(text='緊急連絡先２', font=("Times", 30))
labelpp2.place(x=300, y=500)
labelp2 = tkinter.Label(text='緊急連絡先２の電話番号', font=("Times", 30))
labelp2.place(x=300, y=550)



txt = tkinter.Entry(width=15,  font=("Times", 30)) #名前
txt.place(x=300, y=200)
txtp = tkinter.Entry(width=30, font=("Times", 30)) #連絡先
txtp.place(x=600, y=300)
txtf = tkinter.Entry(width=30, font=("Times", 30)) #家族構成
txtf.place(x=600, y=350)
txtp2 = tkinter.Entry(width=30,  font=("Times", 30)) #緊急連絡先1
txtp2.place(x=800, y=400)
txtp4 = tkinter.Entry(width=30,  font=("Times", 30)) #緊急連絡先2
txtp4.place(x=800, y=500)
txtp1 = tkinter.Entry(width=30,  font=("Times", 30)) #緊急連絡先1tel
txtp1.place(x=800, y=450)
txtp3 = tkinter.Entry(width=30,  font=("Times", 30)) #緊急連絡先2tel
txtp3.place(x=800, y=550)
txtbir = tkinter.Entry(width=20,  font=("Times", 30)) #生年月日
txtbir.place(x=400, y=250)
txtbirj = tkinter.Entry(width=18,  font=("Times", 30)) #生年月日和暦
txtbirj.place(x=820, y=250)
txta = tkinter.Entry(width=3,  font=("Times", 30)) #年齢
txta.place(x=1230, y=250)
txtg = tkinter.Entry(width=3,  font=("Times", 30)) #班
txtg.place(x=200, y=150)

btn = tkinter.Button(root, text='検索', command=btn_click, font=("Times", 20), bg="orange", width=10)
btn.place(x=750, y=750)
btn2 = tkinter.Button(root, text='リセット', command=btn_click_delete, font=("Times", 20), bg="orange", width=10)
btn2.place(x=950, y=750)
        
root.mainloop()
