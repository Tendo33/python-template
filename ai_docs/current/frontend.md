# Current Frontend

## When to read

- 要改 frontend 代码前先读这里。
- 需要了解当前 frontend starter 真实实现和页面范围时读这里。

## Current truth

当前 `frontend/` 是一个很轻的单页 starter，不是完整业务前端。

已经落地的能力：

- React + TypeScript + Vite 前端基础运行链
- Tailwind CSS v4 token 和主题桥接
- 一个基于 `cva` 的 `Button` primitive
- 一个深浅色切换按钮
- 一个简单的 landing page
- Vitest + Testing Library 测试基线

## Current UI scope

当前页面主要用于证明前端基线可工作，而不是提供产品级视觉系统。页面包括：

- 吸顶 header
- 品牌标题
- 主题切换按钮
- hero 文案和 CTA
- 简单 footer

## What is not here yet

- 当前还没有 `frontend/src/features`
- 当前还没有 `frontend/src/lib`
- 当前还没有 `frontend/src/hooks`
- 当前还没有复杂路由、数据层或多页面结构

推荐扩展方向见 [project-structure.md](../reference/project-structure.md)。

## Design system

当前 starter 的视觉和交互规范请从 `ai_docs/INDEX.md` 进入设计系统文档。

## Shared references

- 项目结构见 [project-structure.md](../reference/project-structure.md)
- 验证命令见 [verification.md](../reference/verification.md)
