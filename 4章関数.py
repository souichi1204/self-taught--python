#関数
def f(x):
    return x<10

result=f(2)

#TrueのTは大文字で！
if result==True:
    print("xは10未満")
else:
    print("xは10以上")

#returnの部分をprintに変更しても同じ
def w(x,y,z):
    return x+y+z

#関数定義にreturnがなかったら
def g():
    Z=1+1


#組み込み関数
#lenは文字列の長さを数字で返す関数（この状態で実行されないのはなぜ？）
len("aaa")

#上の物を実行するためにはprint(len("aaa"))=>3
#def lenで関数を作ると上書きされるので注意

#str整数を文字列に変換
str(300)

#intは文字列を整数に変換
int("1")

#小数点以下を示すのはfloat(intだと２と表示される）
float("2.0")


#「lenで変換したものは数値かどうか」を判別する関数
def g(x):
    a=str(x)
    b=len(a)
    return float(b)

#inputはユーザーから情報を受け取る
age=input("Enter your age:")
int_age=int(age)
if int(int_age<=19):
    print("あなたは未成年です")
else:
     print("あなたは成人しています")

#チャレンジ：上のプログラムのエラーを削除

#関数の再利用(同じことを繰り返すときは関数を使おう！）
def even_odd(x):
    if x%2==0:
        print("偶数")
    else:
        print("奇数")

#引数をあらかじめ定めておけば引数の欄が空欄でも大丈夫(引数がなければ２、あればその値に上書きされる。）
def f(x=2):
    return x*2

#関数内のものをグローバル変数にするためには変数定義前にglobalを追加(global x)
x=100
def t():
    global x
    x+=1
    print(x)

#例外処理
print("これは１つ目の数字÷2つ目の数字を行うプログラムです。")



#userが0を入れる可能性を消す
#try:の後には例外が発生するかもしれないが、実行したい処理
try:
    number_a=input("1つ目の数字を入力して下さい:")
    int_number_a=int(number_a)
    number_b=input("2つ目の数字を入力して下さい:")   
    int_number_b=int(number_b)

    print(int_number_a/int_number_b)

#exceptの後には起きうるエラー(2つある場合はまとめて（）で書ける。と起きた場合の処理を記入
except ZeroDivisionError:
    print("２番目の数字に０が入力されています。")
except ValueError:  
    print("数字の入力をお願いします")

#ドキュメンテーション(関数定義の次の行に"""終わりに""")は関数に関するコメントのようなもの
def add(x,y):
    """
    Returns x+y.
    :param x:int.
    :param y:int.
    :return: int sum of x and y.
    """
    return x+y
