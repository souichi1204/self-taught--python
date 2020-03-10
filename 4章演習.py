#1:数値を入力値として受け取り、その数字を二乗して返す関数を作成
#例外処理はしていない。numberの部分に""を付けないで生じるnameerrorの解決策がわからない
def squred(number):    
        int_number=int(number)
        return int_number*int_number

#2:文字列を引数にする関数
def hello(whom):
        return "Hello"+whom

#3:3つの必須引数と２つのオプション引数がある関数    
def third(a,b,c):
        return a+b+c
#3:2つのオプション引数
def Birthday(who="user",age=20):
        return who+"さん"+str(age)+"歳のお誕生日おめでとうございます。"

#4:2つの関数からなるプログラム。
#1つ目：関数は整数を引数として受け取り、その整数を２で割って求められる整数を出力として返す
def waru2(suuti):
        int_suuti=int(suuti)
        return suuti/2
#2つ目:整数を引数として受け取り、４で掛けた整数を返す。
def kake4(kazu):
        int_kazu=int(kazu)
        return int_kazu*4
        
#合体させて１つ目の関数の戻り値を２つ目の引数に移して表示
#=>kake4(waru2(2))==2

#5:文字列をfloat型に変換し、戻り値とする関数を書く。例外処理もして。
def hennkann(mojiretu):
        try:
                return float(mojiretu)
        except ValueError:
                print("文字列が入力されています。数字を入力して下さい")
                """
        mojiretuに””ない時のエラーを下記で処理できないのはなぜ？
        except NameError:
                print("数字を入力して下さい")
        except SyntaxError:
                print("a")
                """



        
        
