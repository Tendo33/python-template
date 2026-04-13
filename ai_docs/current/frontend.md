# Current Frontend

## When to read

- 要改 frontend 代码前先读这里。
- 需要了解当前 frontend starter 的真实范围和可复用入口时读这里。

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

当前页面主要用于证明前端基线可工作，而不是提供完整产品视觉系统。页面包括：

- 吸顶 header
- 品牌标题
- 主题切换按钮
- hero 文案和 CTA
- 简单 footer

## Current frontend structure

- `frontend/src/app`：当前页面入口与测试
- `frontend/src/components`：共享组件与 UI primitives
- `frontend/src/styles`：全局样式与 token
- `frontend/src/test`：测试初始化
- `frontend/src/lib/utils.ts`：当前唯一已落地的通用前端工具
- `frontend/src/features`、`frontend/src/hooks`：目录已预留，但当前还没有业务级实现

## What is not here yet

- 当前还没有复杂路由
- 当前还没有数据获取层或状态管理方案
- 当前还没有多页面结构
- 当前还没有真正的 feature 模块内容

## Shared references

- frontend 约束见 [frontend.md](../standards/frontend.md)
- 设计系统基线见 [design-system.md](../standards/design-system.md)
- 项目结构见 [project-structure.md](../reference/project-structure.md)
- 验证命令见 [verification.md](../reference/verification.md)
