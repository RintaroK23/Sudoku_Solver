# Sudoku_Solver
数独(ナンプレ)を自動で解くプログラムです。

実行すると『問題をスペース、カンマなどを入れずに1行ずつ入力(空欄は0を入力)』と表示されるので、以下の例(参照元:https://nanpre.adg5.com/xlsx_down.php のレベル１問題1)のように問題を入力すると解答が出力されます。<br>
(注)「数独」は株式会社ニコリの登録商標です。

## ex.
問題をスペース、カンマなどを入れずに1行ずつ入力(空欄は0を入力)<br>
605003400  
703005082  
480100605  
924031758  
000908203  
037040096  
569084370  
271300864  
048716020

## 実行結果

入力した問題  
[[6 0 5 0 0 3 4 0 0]  
 [7 0 3 0 0 5 0 8 2]  
 [4 8 0 1 0 0 6 0 5]  
 [9 2 4 0 3 1 7 5 8]  
 [0 0 0 9 0 8 2 0 3]  
 [0 3 7 0 4 0 0 9 6]  
 [5 6 9 0 8 4 3 7 0]  
 [2 7 1 3 0 0 8 6 4]  
 [0 4 8 7 1 6 0 2 0]]  

----------------------  
解答 1  
[[6 9 5 8 2 3 4 1 7]  
 [7 1 3 4 6 5 9 8 2]  
 [4 8 2 1 9 7 6 3 5]  
 [9 2 4 6 3 1 7 5 8]  
 [1 5 6 9 7 8 2 4 3]  
 [8 3 7 5 4 2 1 9 6]  
 [5 6 9 2 8 4 3 7 1]  
 [2 7 1 3 5 9 8 6 4]  
 [3 4 8 7 1 6 5 2 9]]  
