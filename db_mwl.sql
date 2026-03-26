-- [コマンドプロンプトに以下を入力し、MySQLの存在する場所に移動する]
cd \
cd \xampp\mysql\bin

-- [MySQLを起動する方法]
mysql -u root -p


-- [データベースの一覧を確認する]
SHOW DATABASES;


-- [データベースを作成する]
-- [データベースの文字コードを設定]mb4は絵文字使わなかったらなくてもOK
CREATE DATABASE db_mini_wallet_lab
DEFAULT CHARACTER SET utf8mb4;

-- [データベースを指定する]
USE db_mini_wallet_lab;

-- 何かあったときにDB削除
-- 使用中なら、先にDB切り替えてから削除
USE mysql;
drop database db_mini_wallet_lab;
-- テーブル削除
DROP TABLE テーブル名;


-- [テーブルの一覧を確認する]
SHOW TABLES;

