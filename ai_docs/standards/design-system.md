# Frontend Design System

## When to read

- 写任何 UI 代码前先读这里。
- 如果要改版、重构 UI 或扩展视觉语言，先改这里，再改代码。

## Design goal

当前前端不是业务产品，而是模板仓库的演示壳层。设计目标是：

- 让新仓库一 clone 下来就有一个干净、可运行的前端入口
- 展示主题 token、Button primitive、深浅色切换这些最基础的搭建方式
- 保持克制，不抢未来真实产品设计的空间

## Current UI scope

当前只实现了一个单页 landing starter，位于 `frontend/src/app/App.tsx`。页面由以下部分组成：

- 吸顶 header
- 品牌标题 `Python Template`
- 深浅色切换按钮
- 居中的 hero 文案与 CTA
- 简单 footer

## Visual direction

- 中性
- 清爽
- 工具型
- 不做过度品牌化

关键词：

- neutral
- minimal
- technical
- calm

## Token system

所有 token 定义在 `frontend/src/styles/globals.css`，使用 OKLCH 表达，并通过 `@theme inline` 映射到 Tailwind 语义颜色。

当前 token 方向：

- 中性色为主
- 使用 `background`、`foreground`、`primary`、`secondary`、`muted-foreground`、`border` 等语义 token
- 已预留 chart 和 sidebar token，但当前页面还未消费

## Component rules

### Button

- 使用 `class-variance-authority`
- 支持 `asChild`
- 通过 `data-slot`、`data-variant`、`data-size` 暴露语义

### ThemeToggle

- 通过 `.dark` class 切换主题
- 使用图标表达当前动作
- 目前不做本地持久化或系统主题侦测

## Motion and responsive rules

- 当前只用轻量状态过渡
- 不使用弹性或弹跳缓动
- 小屏优先
- 主要依靠阅读宽度与按钮自动换行保持响应式

## Accessibility rules

- 所有可交互元素要有可见 focus 样式
- 主题切换按钮必须保留 `aria-label`
- 颜色不是唯一状态表达方式

## Shared references

- 当前 frontend 现状见 [frontend.md](../current/frontend.md)
- 其它 frontend 约束和 workflow 请从 `ai_docs/INDEX.md` 进入
