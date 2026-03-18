# Frontend Design System

> **本文档是项目前端的唯一视觉/交互规范。**
> 本文件初始为模板。**任何 AI 工具或开发者在编写前端 UI 代码之前，必须先完善本文档中的 `[待定]` 部分。**
> 需要重构或改版 UI 时，**先修改本文档，再实施代码变更。**

---

## 使用流程

```text
1. 收到前端需求
   ↓
2. 逐层完善本文档的 [待定] 部分（L1 → L2 → L3 → L4 → L5）
   ↓
3. 与用户确认设计方向
   ↓
4. 按文档实施代码（tokens → components → patterns → screens）
   ↓
5. 重构时：先改本文档 → 再改代码
```

**禁止跳过第 2 步直接写代码。**

---

## Architecture Overview

```text
┌─────────────────────────────────────────────────────┐
│  Layer 5 — Screens                                  │
│  具体页面: 首页, 设置页, 仪表盘...                      │
├─────────────────────────────────────────────────────┤
│  Layer 4 — Patterns                                 │
│  组合布局: Sidebar, Form, DataTable...               │
├─────────────────────────────────────────────────────┤
│  Layer 3 — Components                               │
│  可复用模块: Button, Card, Input, Dialog...           │
├─────────────────────────────────────────────────────┤
│  Layer 2 — Design Tokens                            │
│  颜色 / 字体 / 间距 / 圆角 / 阴影 / 动效              │
├─────────────────────────────────────────────────────┤
│  Layer 1 — Design Principles                        │
│  UI 规则和原则: 一致性 / 层级 / 可读性 / 意图           │
└─────────────────────────────────────────────────────┘
```

变更自底向上流动：修改原则或 token 会影响上方所有层。

---

## Layer 1 — Design Principles

通用原则适用于所有项目。项目特定原则在下方 `[待定]` 区域补充。

### 1.1 Intentionality over Decoration

每个视觉元素必须有存在理由。如果去掉它不影响清晰度或可用性，就去掉它。

### 1.2 Visual Hierarchy

使用**多个维度**建立层级——尺寸、字重、颜色、位置、留白——不要只靠单一维度。

| 维度 | 强信号 | 弱信号 |
| :--- | :--- | :--- |
| 尺寸 | 3:1 比例以上 | < 2:1 |
| 字重 | Bold vs Regular | Medium vs Regular |
| 颜色 | 高对比 | 相近色调 |
| 位置 | 顶部 / 左侧 | 底部 / 右侧 |
| 留白 | 充裕隔离 | 拥挤 |

### 1.3 Consistency

- 同一术语，同一含义，全局统一。
- 相同元素在所有页面中外观和行为一致。
- 间距、圆角、阴影、颜色只从 L2 tokens 取值，不允许 magic number。

### 1.4 Readability

- 正文最小 `1rem`（16px），行宽最大 `65ch`。
- `line-height` 与行宽成反比——窄列更紧，宽列更松。
- 深色背景上，`line-height` 增加 0.05–0.1，字重减轻。
- 字号使用 `rem`/`em`，禁止 `px` 作为正文字号。

### 1.5 Accessibility

- WCAG 2.1 AA 最低标准。正文 4.5:1 对比度，大字 3:1，UI 组件 3:1。
- 禁止 `user-scalable=no`。
- 所有交互元素有可见 `:focus-visible` 聚焦环。
- 触控目标最小 44px。
- 不依赖颜色单独传达状态。
- 尊重 `prefers-reduced-motion` 和 `prefers-color-scheme`。

### 1.6 Performance

- 低风险操作使用 Optimistic UI。
- 骨架屏优于 spinner。
- 仅动画 `transform` 和 `opacity`，高度用 `grid-template-rows` 过渡。

### 1.7 Mobile-First

- 基础样式面向移动端，`min-width` 媒体查询叠加复杂度。
- 使用 `@container` 做组件级响应式。
- 使用 `pointer` / `hover` 媒体查询检测输入方式而非屏幕尺寸。

### 1.8 Anti-Patterns（硬拒清单）

以下模式在任何项目中都禁止——它们是 AI 生成代码的特征指纹：

- 纯黑 `#000` 或纯白 `#fff`。
- Card 嵌套 Card。
- 重复相同的卡片网格（图标 + 标题 + 描述 × N）。
- 大数字 + 小标签 + 渐变装饰的 Hero Metric 模板。
- 无功能目的的 glassmorphism。
- 弹性 / 弹跳缓动。通用 `ease` 时间函数。
- 等宽字体当"技术风格"的懒惰手段。
- 每个标题上方放大圆角图标。

### 1.9 项目特定原则

> **[待定]** 开始前端开发前，根据项目定位补充：
>
> - **产品调性**：（如：专业严肃 / 活泼友好 / 极简克制 / 大胆前卫）
> - **目标用户**：（如：开发者 / 企业用户 / 普通消费者）
> - **视觉方向**：（如：editorial / brutalist / organic / luxury / playful / industrial）
> - **差异化记忆点**：用户看到界面后会记住什么？
> - **参考项目 / 竞品**：（URL 或截图）

---

## Layer 2 — Design Tokens

所有视觉值以 CSS 自定义属性定义在 `frontend/src/styles/globals.css` 中。
组件不允许使用 token 系统之外的硬编码值。

### 2.1 Color

> **[待定]** 选定项目配色后，填写下表并实现到 `globals.css`。

#### Color space

推荐 OKLCH（感知均匀）。随亮度趋向极值时，降低 chroma。

#### Semantic color tokens

> 以下是需要定义的语义色。值为 `[待定]`，实施前必须填入具体 OKLCH 值。

| Token | 角色 | Light 值 | Dark 值 |
| :--- | :--- | :--- | :--- |
| `--background` / `--foreground` | 页面底色和主文字 | [待定] | [待定] |
| `--card` / `--card-foreground` | 卡片底色和文字 | [待定] | [待定] |
| `--popover` / `--popover-foreground` | 弹出层 | [待定] | [待定] |
| `--primary` / `--primary-foreground` | CTA 和主操作 | [待定] | [待定] |
| `--secondary` / `--secondary-foreground` | 次要操作 | [待定] | [待定] |
| `--muted` / `--muted-foreground` | 弱背景和辅助文字 | [待定] | [待定] |
| `--accent` / `--accent-foreground` | 高亮和激活状态 | [待定] | [待定] |
| `--destructive` / `--destructive-foreground` | 错误和危险操作 | [待定] | [待定] |
| `--border` | 边框和分割线 | [待定] | [待定] |
| `--input` | 输入框边框 | [待定] | [待定] |
| `--ring` | 聚焦环 | [待定] | [待定] |

#### Color rules

- **中性色要染色**：在灰色中加入品牌色相的微量 chroma（0.01 即可）。
- **60-30-10**：60% 中性表面，30% 辅助文字/边框，10% 强调色。
- **禁止灰色叠在彩色背景上**——使用背景色的深浅变体或透明度。
- **暗色模式不是反转亮色模式**：用更亮的表面表示层级（不用阴影），略微降低强调色饱和度，减轻正文字重。

### 2.2 Typography

> **[待定]** 选定字体后，填写下方表格。

#### Font selection

| 用途 | 字体名 | 来源 | 备选 |
| :--- | :--- | :--- | :--- |
| Display / 标题 | [待定] | [待定: Google Fonts / 本地 / 系统] | [待定] |
| Body / 正文 | [待定] | [待定] | [待定] |
| Mono / 代码 | [待定] | [待定] | [待定] |

**选字体时避免**：Inter, Roboto, Arial, Open Sans, Lato, Montserrat（过于通用）。
**推荐替代**：Instrument Sans, Plus Jakarta Sans, Outfit, Onest, Figtree, Urbanist, Fraunces, Newsreader, Lora。
**系统字体也可以**：`-apple-system, BlinkMacSystemFont, "Segoe UI", system-ui` — 原生感、零延迟。

#### Type scale

> 推荐使用模块化比例。选定比例后填入具体值。
> 常用比例：1.25（大三度）、1.333（纯四度）、1.5（纯五度）。

| Token | 尺寸 | 用途 |
| :--- | :--- | :--- |
| `--text-xs` | [待定] | 注释、法律文本 |
| `--text-sm` | [待定] | 元数据、标签 |
| `--text-base` | [待定] | 正文 |
| `--text-lg` | [待定] | 小标题、引导 |
| `--text-xl` | [待定] | 章节标题 |
| `--text-2xl` | [待定] | 页面标题 |
| `--text-3xl` | [待定] | Hero / 展示 |

> 建议使用 `clamp(min, preferred, max)` 实现流式字号，免去断点。

#### Line height

| 场景 | `line-height` | `max-width` |
| :--- | :--- | :--- |
| 正文 | 1.5 – 1.6 | 65ch |
| 标题 | 1.1 – 1.2 | — |
| 紧凑 UI（标签、按钮） | 1.25 | — |

### 2.3 Spacing

> 推荐 4px 基础网格。根据项目调整具体尺度。

| Token | 值 | 用途 |
| :--- | :--- | :--- |
| `--space-1` | `0.25rem` (4px) | 极小间隙 |
| `--space-2` | `0.5rem` (8px) | 组件内部紧凑 |
| `--space-3` | `0.75rem` (12px) | 组件默认内距 |
| `--space-4` | `1rem` (16px) | 兄弟元素标准间距 |
| `--space-6` | `1.5rem` (24px) | 区域分隔（轻） |
| `--space-8` | `2rem` (32px) | 区域分隔（中） |
| `--space-12` | `3rem` (48px) | 大区域分隔 |
| `--space-16` | `4rem` (64px) | 页面级纵向节奏 |
| `--space-24` | `6rem` (96px) | Hero / 特性区域 |

#### Spacing rules

- 用 `gap` 取代 margin 做兄弟间距。
- 通过**变化的间距**创造节奏——紧密分组 + 宽松分隔。
- 大屏上使用 `clamp()` 做流式间距。

### 2.4 Border Radius

> **[待定]** 选定基础圆角后填入。

| Token | 值 | 用途 |
| :--- | :--- | :--- |
| `--radius` | [待定: 如 `0.625rem`] | 基础值 |
| `--radius-sm` | `calc(var(--radius) - 4px)` | Badge, Chip |
| `--radius-md` | `calc(var(--radius) - 2px)` | Input, Dropdown |
| `--radius-lg` | `var(--radius)` | Card, Panel |
| `--radius-xl` | `calc(var(--radius) + 4px)` | Modal, 大容器 |
| `--radius-full` | `9999px` | 药丸形、头像 |

### 2.5 Shadows & Elevation

> **[待定]** 可沿用推荐值或按项目调性调整。

| Token | 推荐值 | 用途 |
| :--- | :--- | :--- |
| `--shadow-xs` | `0 1px 2px oklch(0% 0 0 / 0.05)` | 按钮微浮 |
| `--shadow-sm` | `0 1px 3px oklch(0% 0 0 / 0.1), 0 1px 2px oklch(0% 0 0 / 0.06)` | 静态卡片 |
| `--shadow-md` | `0 4px 6px oklch(0% 0 0 / 0.1), 0 2px 4px oklch(0% 0 0 / 0.06)` | 下拉菜单 |
| `--shadow-lg` | `0 10px 15px oklch(0% 0 0 / 0.1), 0 4px 6px oklch(0% 0 0 / 0.05)` | Modal |

> 暗色模式：用更亮的表面色替代阴影。

#### Z-index scale

| Token | 值 | 用途 |
| :--- | :--- | :--- |
| `--z-dropdown` | `10` | 下拉菜单 |
| `--z-sticky` | `20` | 吸顶栏 |
| `--z-overlay` | `30` | 遮罩层 |
| `--z-modal` | `40` | Modal |
| `--z-toast` | `50` | Toast |
| `--z-tooltip` | `60` | Tooltip |

### 2.6 Motion

| Token | 值 | 用途 |
| :--- | :--- | :--- |
| `--duration-instant` | `100ms` | 按下、开关、变色 |
| `--duration-fast` | `200ms` | Hover、Tooltip |
| `--duration-normal` | `300ms` | 菜单、手风琴、抽屉 |
| `--duration-slow` | `500ms` | 页面入场、Hero |

| Token | 值 | 用途 |
| :--- | :--- | :--- |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | 元素进入 |
| `--ease-in` | `cubic-bezier(0.7, 0, 0.84, 0)` | 元素退出 |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | 状态切换 |
| `--ease-out-quart` | `cubic-bezier(0.25, 1, 0.5, 1)` | 默认微交互 |

退出动画用进入时长的 **75%**。

### 2.7 Breakpoints

| Token | 值 | 用途 |
| :--- | :--- | :--- |
| `--bp-sm` | `640px` | 大手机横屏 / 小平板 |
| `--bp-md` | `768px` | 平板 |
| `--bp-lg` | `1024px` | 桌面 |

> 优先 `clamp()` 和 container query，断点仅用于布局切换。

---

## Layer 3 — Components

组件位于 `frontend/src/components/ui/`（shadcn 基础组件）和 `frontend/src/components/`（自定义共享组件）。

### 3.1 Component Architecture

```bash
# shadcn 基础组件——优先从 registry 添加
pnpm --prefix frontend dlx shadcn@latest add <component>
```

自定义组件规范：
- 使用 `cn()` (`@/lib/utils`) 做 class 合并。
- 使用 `cva` (class-variance-authority) 管理 variant。
- Named export。`data-slot` 标注根元素。
- 扩展原生元素用 `React.ComponentProps<"element">`。
- `ref` 需要时必须 forward。

#### File structure

```text
ComponentName.tsx        # 实现
ComponentName.test.tsx   # 测试（可选，就近放置）
```

### 3.2 Component Catalog

> **[待定]** 项目开发过程中，将已使用/已安装的组件登记到下表。
> 新增组件前先查本表，避免重复。

| 组件名 | 来源 | Variants | 备注 |
| :--- | :--- | :--- | :--- |
| `Button` | shadcn | [待定: 列出使用的 variant] | |
| | | | |
| | | | |

> 随项目推进逐步填充。每次 `shadcn add` 或自建组件后更新此表。

### 3.3 Interactive State Design

每个交互组件必须实现以下状态：

| 状态 | 视觉处理 | 是否必须 |
| :--- | :--- | :--- |
| Default | Token 基础样式 | 是 |
| Hover | 微妙颜色变化，无布局偏移。仅 `@media (hover: hover)` | 是 |
| Focus-visible | `2px solid var(--ring)`，`2px` offset，3:1 对比 | 是 |
| Active / Pressed | 更深色调或 `scale(0.98)` | 是 |
| Disabled | `opacity: 0.5`, `pointer-events: none` | 是 |
| Loading | 内联 spinner 或骨架屏替代 | 异步时 |
| Error | `--destructive` 边框 + icon + 消息 via `aria-describedby` | 可验证时 |
| Success | 短暂成功反馈 | 可确认时 |

### 3.4 UX Writing Rules

| 原则 | 规则 | 示例 |
| :--- | :--- | :--- |
| 按钮文案 | 动词 + 宾语，禁止 "确定"、"提交"、"是/否" | "保存更改"、"删除项目" |
| 破坏性确认 | 说明操作 + 后果 | "删除 5 个项目？此操作不可撤回。" |
| 错误消息 | 发生了什么 + 为什么 + 怎么修 | "邮箱需要 @ 符号。示例：name@domain.com" |
| 空状态 | 说明 + 价值 + 行动 | "还没有项目。创建第一个开始使用。" |
| 加载文案 | 具体描述 | "正在保存草稿…" 而非 "加载中…" |
| 术语一致 | 每个概念只用一个词 | 删除（不混用 移除 / 清除），设置（不混用 偏好 / 选项） |

---

## Layer 4 — Patterns

Pattern 是由 L3 组件 + L2 tokens 组合而成的**复合布局**。
放在 `frontend/src/components/`（共享）或 `frontend/src/features/<feature>/`（领域内）。

### 4.1 Pattern Catalog

> **[待定]** 根据项目需要，选择并定义所需的 Pattern。
> 以下是常见 Pattern 模板。项目不需要的可以删除，需要新增的按格式添加。

#### AppShell（应用外壳）

> 根布局容器。根据项目需要选择有无 sidebar。

```text
┌──────────────────────────────────────────────┐
│ Header (sticky, backdrop-blur)               │
├────────┬─────────────────────────────────────┤
│ Side-  │ Main content area                   │
│ bar    │                                     │
│ (可选) │                                     │
├────────┴─────────────────────────────────────┤
│ Footer (可选)                                │
└──────────────────────────────────────────────┘
```

- Header: `sticky top-0`, `z-[var(--z-sticky)]`, `bg-background/80 backdrop-blur-sm`。
- Sidebar: 可折叠。移动端用 `Sheet`，桌面端常驻。
- Main: `flex-1`，container 限宽，页面级 padding。

#### FormPattern（表单）

- 使用 `react-hook-form` + `zod` 做校验。
- Label 始终可见在 Input 上方（禁止用 placeholder 当 label）。
- Blur 时验证，非逐键（密码强度除外）。
- 相关字段用 `<fieldset>` + `<legend>` 分组。
- Error 在字段下方，`aria-describedby` 关联。
- 主操作按钮右下，取消按钮在其左侧。

#### DataTable（数据表格）

- `@tanstack/react-table` 做 headless 逻辑。
- 数字列 `font-variant-numeric: tabular-nums`。
- 响应式：移动端转卡片布局或固定首列横向滚动。
- 空状态带明确操作引导。

#### SearchCommand（搜索 / 命令面板）

- `Cmd+K` / `Ctrl+K` 触发。
- shadcn `Command` 组件。
- 分类结果 + 键盘导航。

#### DashboardGrid（仪表盘网格）

- `repeat(auto-fit, minmax(280px, 1fr))` 自适应网格。
- 禁止完全相同的卡片重复——变化卡片尺寸，feature metric 占 2 列。
- 骨架屏加载态。

#### ConfirmDialog（确认对话框）

- **优先使用 undo 而非 confirm**。仅用于不可逆操作。
- 标题命名操作，正文说明后果，按钮用具体标签。

### 4.2 Responsive Adaptation

> **[待定]** 列出项目中使用的 Pattern 及其在不同断点的行为。

| Pattern | Mobile (< 640px) | Tablet (640–1024px) | Desktop (> 1024px) |
| :--- | :--- | :--- | :--- |
| [待定] | [待定] | [待定] | [待定] |

### 4.3 Creating New Patterns

1. 确认无法通过已有 Pattern 组合满足需求。
2. 只使用 L3 组件和 L2 tokens 构建。
3. 在本文件中记录：ASCII 布局图 + 响应式行为 + 无障碍要求。
4. 共享 Pattern → `frontend/src/components/`；领域专用 → `frontend/src/features/<feature>/`。

---

## Layer 5 — Screens

Screen 是由 L4 Pattern + L3 组件 + L2 tokens 组合的具体页面。
位于 `frontend/src/app/`（顶级路由）或 `frontend/src/features/<feature>/pages/`（功能路由）。

### 5.1 Screen Checklist

每个页面实现前必须确认：

- [ ] **路由**：定义在 router 中，lazy-loading。
- [ ] **标题**：设置 `document.title`。
- [ ] **布局**：使用 AppShell。
- [ ] **加载态**：骨架屏。
- [ ] **错误态**：Error boundary + 重试。
- [ ] **空状态**：有意义的文案 + 主操作。
- [ ] **响应式**：三个断点验证。
- [ ] **键盘导航**：所有交互元素可通过 Tab / 方向键到达。
- [ ] **焦点管理**：导航后焦点逻辑移动。

### 5.2 Screen Catalog

> **[待定]** 项目开发过程中逐步添加。

| 页面名 | 路由 | 使用的 Patterns | 使用的 Components | 页面状态 |
| :--- | :--- | :--- | :--- | :--- |
| [待定] | [待定] | [待定] | [待定] | [待定] |

### 5.3 Creating New Screens

1. 定义路由、目的、所需状态。
2. 从 L4 选择 Pattern 组合，不从零发明。
3. 在 5.2 Screen Catalog 中登记。
4. 实现到对应目录：
   - `frontend/src/app/` — 顶级路由。
   - `frontend/src/features/<feature>/pages/` — 功能路由。
5. 对照 5.1 Checklist 验证。

---

## Appendix A — File Structure

```text
frontend/src/
├── app/                    # 应用外壳、路由、providers（L5 顶级页面）
├── features/               # 领域模块（L5 功能页面 + L4 功能 Pattern）
│   └── <feature>/
│       ├── pages/
│       ├── components/
│       ├── hooks/
│       └── lib/
├── components/
│   ├── ui/                 # shadcn/ui 基础组件（L3）
│   └── <pattern>.tsx       # 共享 Pattern（L4）
├── hooks/                  # 全局 hooks
├── lib/                    # 工具函数、API client
│   └── utils.ts            # cn()
├── styles/
│   └── globals.css         # Design Tokens（L2）
└── test/                   # 测试基础设施
```

## Appendix B — Decision Log

> 记录偏离或扩展 design system 的决策。

| 日期 | 决策 | 理由 |
| :--- | :--- | :--- |
| [待定] | [待定] | [待定] |

## Appendix C — Quick Reference: 填写顺序

开始新项目的前端时，按此顺序填写 `[待定]` 部分：

1. **L1.9** — 项目调性、目标用户、视觉方向
2. **L2.1** — 配色方案（OKLCH 值）
3. **L2.2** — 字体选择、字号比例
4. **L2.4** — 基础圆角值
5. **L2.5** — 阴影（可沿用推荐值）
6. **L3.2** — 登记首批需要的组件
7. **L4.1** — 选择需要的 Pattern
8. **L4.2** — 填写响应式行为表
9. **L5.2** — 登记第一批页面
10. **Appendix B** — 记录任何偏离决策
