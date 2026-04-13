# Frontend Design System

## When to read

- 写任何 UI 代码前先读这里。
- 如果要改版、重构 UI 或扩展视觉语言，先改这里，再改代码。

## Design sourcing workflow

在开始新的 UI 设计工作前，先用外部 `DESIGN.md` 作为风格起点，再回到仓库约束执行：

1. 先去 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 选择一个适合作为起点的网站风格。
2. 如果没有更明确的参考，默认可先用 Linear 风格，保持简洁、克制、偏产品化的起步状态。
3. 进入对应的 `getdesign.md` 页面，从项目根目录安装该风格的 `DESIGN.md`。
4. Linear 示例命令：`npx getdesign@latest add linear.app`
5. 安装完成后，明确要求 AI assistant 在后续 UI 工作中使用项目根目录的 `DESIGN.md`。

说明：

- `getdesign.md` 提供的是受目标网站启发的 curated starting point，不是官方设计系统。
- 项目根目录存在 `DESIGN.md` 时，UI 风格实现优先遵循它；本文件继续约束仓库内的技术栈、可访问性、响应式和实现边界。
- 如果外部 `DESIGN.md` 与仓库现状冲突，优先保持可运行、可访问、可测试，并把必要差异回写到本文件。

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

如果项目根目录已经安装了外部 `DESIGN.md`，以上方向只作为 starter 默认基线；实际 UI 风格以该 `DESIGN.md` 为准。

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
- 其它 frontend 约束见 [frontend.md](frontend.md)
