from bmi_calc.bmi import Bmi


def main():
    bmi = Bmi(float(input("몸무게")),float(input("키")),input("이름 입력"))

    print("{}님의 BMI지수는 {}입니다".format(bmi.name,bmi.bmi()))


if __name__ == '__main__':
    main()