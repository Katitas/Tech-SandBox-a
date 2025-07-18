# 技術確認課題 – フルスタック Web アプリケーション

本課題は **IT 技術力の確認** を目的とした課題です。7/28までに小規模なフルスタック Web アプリケーションを構築してください。課題は **段階式** になっております。

---

## 1. 目的（確認対象）

| # | 技能領域            | 確認ポイント                                                       |
| - | --------------- | ------------------------------------------------------------ |
| 1 | **バックエンド開発**    | FastAPI ルーティング設計、SQLAlchemy モデル、Alembic マイグレーション、クリーンアーキテクチャ |
| 2 | **フロントエンド開発**   | React + TypeScript のコンポーネント設計、状態管理、API 連携、UI/UX              |
| 3 | **インフラ構築**      | Dockerfile 最適化、`docker-compose.yaml` 設計、環境変数管理               |
| 4 | **GitHub 運用**   | ブランチ戦略、コミット粒度、Pull Request の質、Issues/Projects 活用             |
| 5 | **ドキュメント & DX** | README の明快さ、スクリプト/Makefile、オンボーディング時間                        |

---

## 2. 技術スタック（固定）

* **バックエンド** : FastAPI · SQLAlchemy · Alembic
* **フロントエンド** : React
* **データベース** : PostgreSQL（Docker コンテナ）
* **インフラ** : Docker / Docker Compose（最新版）、`.env` による設定
* **バージョン管理** : Git · GitHub
* **任意ツール** : Pytest, Flake8, Ruff, MyPy, Prettier, ESLint, GitHub Actions など

> **注記:** 上記コア技術の置き換え・削除は禁止です。追加ライブラリは自由に導入して構いません。

---

## 3. 仕様テーマ

**タスク管理アプリ** を実装します。次の機能を段階的に追加してください。

### 基本機能 (ステージ 1 〜 3 内で実装)
- タスク作成（タイトル必須、説明任意）
- タスク一覧取得
- タスク更新（タイトル・説明・完了フラグ）
- タスク削除

### 拡張機能 (ステージ 4 〜 5 で順次実装)
- 期限 (due_date) と 優先度 (priority) の追加
- タグ付け とタグによるフィルタリング
- 検索（タイトル & 説明） + 並び替え（期限・優先度）
- ページネーション（API レスポンス & UI）
- リアルタイム更新：WebSocket または SSE を用いた他クライアントへのイベント配信
- アーカイブ機能：完了済タスクをアーカイブ／復元
- 認証：JWT などを利用した簡易ユーザ認証

---

## 4. ステージ別要件

| ステージ                   | 内容                                                                                                        | 必須区分    |
| ---------------------- | --------------------------------------------------------------------------------------------------------- | ------- |
| **0 – プロジェクトブートストラップ** | リポジトリを「git clone」し開発環境を構築。用意されている環境を起動                                                                        | ✅ 必須    |
| **1 – API & DB**       | Task モデル設計、Alembic マイグレーション作成、FastAPI で CRUD エンドポイント実装（JSON 返却）。                                          | ✅ 必須    |
| **2 – コンテナ化**          | バックエンド用 **`Dockerfile`** 作成。`docker-compose.yaml` で `backend`・`frontend`（作成済みなら）・`db` サービスを定義。`.env` で設定。 | ✅ 必須    |
| **3 – フロント UI**        | - React アプリ - タスク一覧／作成／更新／削除 UI 実装- Axios/Fetch でバックエンドと通信                                          | ✅ 必須    |
| **4 – 拡張機能①**       | - モデルに due_date, priority を追加しマイグレーション- タイトル & 説明検索、完了フィルタ、並び替え（期限・優先度）API 実装- フロント側で対応 UI を追加                                     | 時間があれば |
| **5 – 拡張機能② & CI**           | - タグ付け・タグフィルタを実装- ページネーション（/tasks?limit=10&offset=20 など）- Pytest・Vitest、Lint/Format を追加し GitHub Actions で自動実行                | 時間があれば |
| **6 – リアルタイム & 追加 DX**           | - WebSocket(SSE) を用いてタスク変更イベントを push- 完了タスクのアーカイブ/復元 API + UI- 認証（JWT）を追加し、ユーザ別タスク管理（時間が許せば）               | 時間があれば |

---

## 5. ブランチ & PR ポリシー

1. 既定ブランチ `main`（`master`）への **直接 push を禁止** します。
2. 作業は `<type>/<topic>` 形式の短命ブランチで行ってください（例: `feat/api-crud`, `fix/docker-env`）。
3. Pull Request (PR) は **早く・小さく** 出すこと。

   * 1 PR = 1 論理的変更。
   * タイトルと本文に「何を」「なぜ」を明記。
   * CI が通ってからマージ。
4. マージ方式は **Squash & Merge** を推奨（自己レビュー可）。

---

## 6. 確認したいポイント

| カテゴリ      | 主な観点                                          |
| --------- | --------------------------------------------- |
| 機能実装      | 必須ステージを満たすか、ビジネスロジックの妥当性                      |
| コード品質     | 可読性、設計、命名、一貫性、例外処理、型定義                        |
| インフラ      | Docker イメージサイズ、マルチステージビルド、環境分離、Compose の使いやすさ |
| Git 運用    | ブランチ運用、コミットメッセージ、PR 文化、CI 活用                  |
| DX・ドキュメント | README の明瞭さ、セットアップ速度、補助スクリプト                  |

---

## 7. 成果物 & 提出方法

1. **README** – セットアップ手順をワンライナーで実行できるようにしてください。

   ```bash
   git clone <your-repo>
   cd project
   cp .env.example .env
   docker compose up --build -d
   ```
2. **動作デモ** – Markdown の GIF や画像リンクで十分です（動画不要）。
3. **作業時間ログ**（任意） – 作業配分を簡単な表で残してもらえると助かります。

---

## 8. 開始手順

1. このリポジトリを **Clone**。
2. `python -m venv .venv && source .venv/Scripts/activate && pip install -r backend/requirements.txt` でPython環境整備。
3. `Node.js(10.9.2) install (https://qiita.com/taiponrock/items/9001ae194571feb63a5e)`
3. `cd frontend && npm install` package.json からパッケージをインストール
4. backend 起動方法 : `cd backend && uvicorn app.main:app --reload`
5. ステージ 1 から着手し、小刻みにコミットしてください。

---
