# C言語リファレンス
## main関数
c言語で最初に実行される関数
ロード時に必ずmian関数のoffsetが先頭になる
```
(gdb) start
Temporary breakpoint 1 at 0x40112a
Starting program: /home/fedora/app/c/a.out 
Missing separate debuginfos, use: dnf debuginfo-install glibc-2.30-5.fc31.x86_64

Temporary breakpoint 1, 0x000000000040112a in main ()
```
## 記述方法
- int main (void) {}
- int main (int argc, char *argv[]) {}
- int main (int argc, char **argv) {}
    - int argc:コマンドラインに記述されたパラメータの数
    - char *argv[]: ポインタ配列
    - char **argv: ダブルポインタ（ポインタ配列とかわらない）
## 型
| 型名   | 説明               |
| ------ | ------------------ |
| void   | 型なし             |
| char   | 文字型             |
| int    | 整数型             |
| float  | 単精度浮動小数点型 |
| double | 倍精度浮動小数点型 |
| struct | 構造体             |
| union  | 共用体             |
| enum   | 列挙型             |
## データ型
| 種類         | データ型               | データ型の名称       | バイト長 | 値の範囲
| ------       | ---------------------- | -------------------- | -------- | ------------------------------------------------- |
| 型なし       | void                   | void型               | -        | -                                                 |
| 文字列       | (unsigned) char        | (符号なし)文字型     | 1        | 0~255                                             |
| 文字列       | signed char            | 符号付き文字型	   | 1        | -128~127                                          |
| 整数型       | unsigned short int     | 符号なし短整数型     | 2        | 0～65535                                          |
| 整数型       | (signed) short int     | (符号付き)短整数型   | 2        | -32768～32767                                     |
| 整数型       | unsigned int           | 符号なし整数型       | 4        | 0～4294967295                                     |
| 整数型       | (signed) int           | (符号付き)整数型     | 4        | -2147483648～2147483647                           |
| 整数型       | unsigned long int      | 符号なし長整数型     | 4        | 0～4294967295                                     |
| 整数型       | (signed) long int      | (符号付き)長整数型   | 4        | -2147483648～2147483647                           |
| 整数型       | unsigned long long int | 符号なし長長整数型   | 8        | 0～18446744073709551615                           |
| 整数型       | (signed) long long int | (符号付き)長長整数型 | 8        | -9223372036854775808～9223372036854775807         |
| 浮動小数点型 | float                  | 単精度浮動小数点型   | 4        | 最小の正の数：1.175494e-38 最大値：3.402823e+38   |
| 浮動小数点型 | double                 | 倍精度浮動小数点型   | 8        | 最小の正の数：2.225074e-308 最大値：1.797693e+308 |
## 型修飾子
| 型修飾子 | 説明         |
| -------- | ------------ |
| short    | 短           |
| long     | 長           | 
| signed   | 符号付き     |
| unsigned | 符号なし     |
| const    | 定数化       | 
| restrict | 最適化を促進 |
| volatile | 最適化を抑制 |
## フォーマット指定子
| 入力 | 出力 | 指定子| 対応する型                               | 説明                               |
| ---- | ---- | ----- | ---------------------------------------- | ---------------------------------- |
| ○   |      | %c    | char                                     | １文字を出力する                   |
| ○   |      | %s    | char *                                   | 文字列を出力する                   |
| ○   |      | %d    | int, short                               | 整数を10進で出力する               |
| ○   |      | %u    | unsigned int, unsigned short             | 符号なし整数を10進で出力する       |
| ○   |      | %o    | int, short,unsigned int, unsigned short  | 整数を8進で出力する                |
| ○   |      | %x    | int, short, unsigned int, unsigned short | 整数を16進で出力する               |
| ○   |      | %f    | float                                    | 実数を出力する                     |
| ○   |      | %e    | float                                    | 実数を指数表示で出力する           |
| ○   |      | %g    | float                                    | 実数を最適な形式で出力する         |
| ×   |      | %hd   | short                                    | 単精度整数を10進数として入力する   |
| ○   |      | %ld   | long                                     | 倍精度整数を10進で出力する         |
| ○   |      | %lu   | unsigned long                            | 符号なし倍精度整数を10進で出力する |
| ○   |      | %lo   | long, unsigned long                      | 倍精度整数を8進で出力する          |
| ○   |      | %lx   | long, unsigned long                      | 倍精度整数を16進で出力する         |
| ○   |      | %lf   | double                                   | 倍精度実数を出力する               |
## 記憶域クラス
| 記憶域クラス名 | 説明                                              |
| -------------- | ------------------------------------------------- |
| extern         | 複数のソースファイルで1つの変数を共有する         |
| static         | ファイルの有効範囲内:他のソースファイルから隠ぺい |
|                | ブロックの有効範囲内:前の値を保存                 |
| auto           | 一般的に省略                                      |
| register       | レジスタを使用                                    |
| typedef        | データ型に別名を付ける                            |
## プリプロセッサ
- #include
    - ファイルを取り込む
- #define
    - 文字列の置き換え
- #undef
    - #defineによる文字列置き換えの取り消し
- #ifdef
    - 識別子が定義されているかどうかの判定
- #ifndef
    - 識別子が定義されていないかどうかの判定
- #endif
    - #ifdef、#ifndefなどによる処理ブロックの最後を明示
- #if～#elif～#else～#endif
    - 複雑な判定
## プロトタイプ宣言
- static bool show_date (const char *, struct timespec, timezone_t);
## タイプデフ
typedef 新しい型の形 新しい型名
## 構造体
struct
## 関数
- static bool show_date (const char *format, struct timespec when, timezone_t tz){}
## グローバル変数とローカル変数
- グローバル変数
    - 複数の関数で使用できる変数
- ローカル変数
    - 関数内でのみ使用できる変数
# ポインタ
- &演算子
    - 変数のアドレスを返す。
# ライブラリ関数
## 時刻／日付管理
## メモリ操作
## 疑似乱数操作
## 入出力操作
## 文字列処理操作
## 文字処理操作
## 算術処理操作
## その他

