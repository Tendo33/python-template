# Frontend Development Standards

本文档定义这个仓库的前端默认基线，并区分“当前 starter 已经存在什么”和“项目长大后推荐怎么扩展”。

> 写任何 UI 代码前，先读 [`ai_docs/frontend_design/DESIGN_SYSTEM.md`](frontend_design/DESIGN_SYSTEM.md)。
> 如果要改版或重构 UI，先改设计系统文档，再改代码。

## 固定技术栈

| 层 | 选择 |
| :--- | :--- |
| Package manager | `pnpm` |
| Framework | React 19 |
| Language | TypeScript (`strict`) |
| Bundler | Vite 8 |
| Styling | Tailwind CSS v4 |
| Component pattern | shadcn/ui |
| Test stack | Vitest + Testing Library + jsdom |

除非用户明确要求，否则不要改这套栈。

## 当前 starter 真实状态

当前 `frontend/` 还是一个很轻的单页 starter，不是完整业务前端。实际存在的关键文件：

```text
frontend/
├── components.json
├── src/app/App.tsx
├── src/components/theme-toggle.tsx
├── src/components/ui/button.tsx
├── src/main.tsx
├── src/styles/globals.css
├── src/test/setup.ts
├── vite.config.ts
└── vitest.config.ts
```

当前已经落地的能力：

- `@` -> `frontend/src` 路径别名
- `globals.css` 中的 OKLCH 设计 token
- 一个基于 `cva` 的 `Button`
- 一个深浅色切换按钮
- 一个简单的 landing page

当前还没有这些目录：

- `frontend/src/features`
- `frontend/src/lib`
- `frontend/src/hooks`

所以文档里不能把它们写成“已经存在”。如果需要扩展，再按下面的推荐约定新增。

## 推荐扩展目录

当页面和业务开始增多时，按这个方向演进：

```text
frontend/src/
├── app/            # app shell、路由、providers
├── features/       # 领域模块
├── components/ui/  # shadcn primitives
├── components/     # 自定义共享组件
├── hooks/          # 全局 hooks
├── lib/            # 工具函数、API wrappers
├── styles/         # 全局样式与 token
└── test/           # 测试基础设施
```

## shadcn/ui 约定

- 共享视觉原子优先沿用 shadcn/ui 组件模式
- 新组件优先组合，不要复制粘贴一堆近似 JSX
- registry 安装命令：

```bash
pnpm --prefix frontend dlx shadcn@latest add <component>
```

当前 `components.json` 已经预留了这些 alias：

- `@/components`
- `@/components/ui`
- `@/lib`
- `@/hooks`

注意：alias 已经预留，不代表目录已经存在。

## TypeScript 与样式规则

- 保持 `strict` 开启
- 默认不使用 `any`
- token 写在 `frontend/src/styles/globals.css`
- 当前 starter 把 `cn()` 实现在 `button.tsx` 内部；当第二个共享组件也需要 class 合并时，再提取到 `frontend/src/lib/utils.ts`
- 样式优先消费语义 token，例如 `bg-background`、`text-muted-foreground`、`border-border`

## 测试与质量

- 组件测试使用 Vitest + Testing Library
- 交互测试优先 `userEvent`
- starter 现在只覆盖了 `App` 的基本渲染，后续新增组件时同步补测试

必跑命令：

```bash
pnpm --prefix frontend lint
pnpm --prefix frontend typecheck
pnpm --prefix frontend test
pnpm --prefix frontend build
```

## README 约定

顶层 README 的前端部分应该：

- 明确这是一个 starter，而不是完整业务系统
- 写清当前已经有的页面和组件
- 把运行命令放进可复制代码块
- 如果提到未来目录结构，要标成“推荐扩展约定”
