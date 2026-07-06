# 🐉 SagaSmith AI

<p align="center">
  <img src="sagasmith.png" alt="SagaSmith" width="200">
</p>

<p align="center">
  <b>让 AI 成为你的地下城主</b><br>
  Turn AI into your Dungeon Master
</p>

<p align="center">
  <a href="https://SagaSmithAI.github.io">🌐 官网</a> ·
  <a href="https://github.com/SagaSmithAI">📦 所有仓库</a>
</p>

---

## 生态 / Ecosystem

| 仓库 | 定位 | Role |
|------|------|------|
| 🏗️ [sagasmith-core](https://github.com/SagaSmithAI/Sagasmith-core) | 通用引擎 — DB、文档、RAG、FTS5、快照 | System-neutral engine |
| ⚔️ [sagasmith-dnd](https://github.com/SagaSmithAI/Sagasmith-dnd) | D&D 5e 2014/2024 运行时 + CLI + HTTP API | D&D 5e runtime + API |
| 🕯️ [sagasmith-coc](https://github.com/SagaSmithAI/Sagasmith-coc) | CoC 7e 运行时 + CLI | CoC 7e runtime |
| 🖥️ [sagasmith-dnd-ui](https://github.com/SagaSmithAI/sagasmith-dnd-ui) | D&D 管理面板 — Astro + React | D&D admin dashboard |
| 🖥️ [sagasmith-coc-ui](https://github.com/SagaSmithAI/sagasmith-coc-ui) | CoC 守秘人面板 — Astro + React | CoC Keeper dashboard |
| 📦 [SagaSmith-dnd-skills](https://github.com/SagaSmithAI/SagaSmith-dnd-skills) | D&D Agent Skills（完整版 + Standalone） | D&D skill defs |
| 📦 [SagaSmith-coc-skills](https://github.com/SagaSmithAI/SagaSmith-coc-skills) | CoC Agent Skills（完整版 + Standalone） | CoC skill defs |
| ✍️ [SagaSmith-module-gen-skills](https://github.com/SagaSmithAI/SagaSmith-module-gen-skills) | 冒险模组生成器（25 种范式） | Module generator |

---

## 安装 / Install

用户告诉 Agent 一个 URL，Agent 自动处理：

> **"帮我装 https://github.com/SagaSmithAI/SagaSmith-dnd-skills"**

Agent 会：
1. 问你选 **完整版** 还是 **轻量版**
2. 完整版 → `pip install` + 加载 `full/SKILL.md`
3. 轻量版 → 切 `standalone/` + `python portable.py` 零依赖运行

---

## 功能 / Features

| 功能 | 完整版 | Standalone |
|------|:---:|:---------:|
| 持久化战役 / Persistent campaigns | ✅ SQLite | ✅ JSON 文件 |
| PDF 模组导入 / PDF module import | ✅ | ❌（Markdown only） |
| FTS5 全文检索 / Full-text search | ✅ BM25 | ✅ 词法评分 |
| ChromaDB 语义搜索 / Semantic search | ✅ 可选 | ❌ |
| Snapshot DAG 存档 / Snapshot saves | ✅ | ✅ 目录快照 |
| 管理面板 / Admin dashboard | ✅ serve API | ❌ |
| 角色管理 / Character management | ✅ | ✅ |
| 战斗引擎 / Combat engine | ✅ d20 | ✅ d20 |
| CoC d100 成功等级 / d100 success levels | ✅ | ✅ |
| 零依赖 / Zero deps | ❌ | ✅ |

---

## 许可证 / License

代码 MIT。D&D 5e SRD 5.2.1 © Wizards of the Coast，以 [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) 授权使用。
