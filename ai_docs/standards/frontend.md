# Frontend Standards

## When to read

- frontend 任务开始前必读。
- 改 UI 前先读这里，再读设计系统。
- 如果项目根目录有 `DESIGN.md`，改 UI 前也要一起读，并把它当作视觉实现输入。

## Fixed stack

- `pnpm`
- React 19
- TypeScript (`strict`)
- Vite 8
- Tailwind CSS v4
- shadcn/ui 组件模式
- Vitest + Testing Library + jsdom

除非用户明确要求，否则不要改这套栈。

## Working rules

- 共享视觉原子优先沿用 shadcn/ui 组件模式
- 当前 starter 还是单页壳层，不要把未来结构写成当前实现
- 当第二个以上共享组件需要通用工具时，再继续扩展 `frontend/src/lib`
- 样式优先消费语义 token，不直接硬编码色值
- 视觉风格优先级为：项目根目录 `DESIGN.md` > `ai_docs/standards/design-system.md` 的默认基线 > 临时发挥

## TypeScript and UI rules

- 保持 `strict`
- 默认不使用 `any`
- 组件和页面改动要考虑响应式与可访问性
- 如果改视觉或交互系统，先更新设计系统文档

## Testing rules

- 组件测试用 Vitest + Testing Library
- 交互测试优先 `userEvent`
- starter 当前测试很轻，新增组件时同步补测试

## Shared references

- 当前 frontend 现状见 [frontend.md](../current/frontend.md)
- 项目结构见 [project-structure.md](../reference/project-structure.md)
- 验证命令见 [verification.md](../reference/verification.md)
- 设计系统基线见 [design-system.md](design-system.md)
