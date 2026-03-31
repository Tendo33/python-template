# Frontend Design System

本文档是当前前端 starter 的唯一视觉 / 交互规范。后续任何 UI 改动，都应该先更新这里，再动代码。

## 1. 设计目标

当前前端不是业务产品，而是模板仓库的演示壳层。它的设计目标很明确：

- 让新仓库一 clone 下来就有一个干净、可运行的前端入口
- 展示主题 token、Button primitive、深浅色切换这些最基础的搭建方式
- 保持克制，不抢未来真实产品设计的空间

## 2. 当前界面范围

当前只实现了一个单页 landing starter，位于 `frontend/src/app/App.tsx`。

页面由四部分组成：

1. 吸顶 header
2. 品牌标题 `Python Template`
3. 深浅色切换按钮
4. 居中的 hero 文案、两个 CTA、页脚

这个页面的任务是“证明前端基线可工作”，不是提供完整产品 UI。

## 3. 视觉方向

### 产品调性

- 中性
- 清爽
- 工具型
- 不做过度品牌化

### 目标用户

- 开发者
- 使用本仓库快速起项目的人

### 视觉关键词

- neutral
- minimal
- technical
- calm

### 差异化边界

当前 starter 不追求强记忆点，而追求“低阻力接管”。真正的产品视觉识别应在项目生成后再建立。

## 4. Token System

所有 token 定义在 `frontend/src/styles/globals.css`，使用 OKLCH 表达，并通过 `@theme inline` 映射到 Tailwind 语义颜色。

### 4.1 色彩

当前使用 shadcn New York neutral 风格的中性色方案。

| Token | Light | Dark |
| :--- | :--- | :--- |
| `--background` | `oklch(1 0 0)` | `oklch(0.145 0 0)` |
| `--foreground` | `oklch(0.145 0 0)` | `oklch(0.985 0 0)` |
| `--card` | `oklch(1 0 0)` | `oklch(0.145 0 0)` |
| `--primary` | `oklch(0.205 0 0)` | `oklch(0.985 0 0)` |
| `--primary-foreground` | `oklch(0.985 0 0)` | `oklch(0.205 0 0)` |
| `--secondary` | `oklch(0.97 0 0)` | `oklch(0.269 0 0)` |
| `--muted-foreground` | `oklch(0.556 0 0)` | `oklch(0.708 0 0)` |
| `--border` | `oklch(0.922 0 0)` | `oklch(0.269 0 0)` |
| `--input` | `oklch(0.922 0 0)` | `oklch(0.269 0 0)` |
| `--ring` | `oklch(0.708 0 0)` | `oklch(0.439 0 0)` |
| `--destructive` | `oklch(0.577 0.245 27.325)` | `oklch(0.396 0.141 25.723)` |

补充 token：

- `--chart-1` 到 `--chart-5`
- `--sidebar-*`

这些 token 已经预留，但当前 starter 页面本身还没有图表或 sidebar。

### 4.2 圆角

| Token | 值 |
| :--- | :--- |
| `--radius` | `0.625rem` |
| `--radius-sm` | `calc(var(--radius) - 4px)` |
| `--radius-md` | `calc(var(--radius) - 2px)` |
| `--radius-lg` | `var(--radius)` |
| `--radius-xl` | `calc(var(--radius) + 4px)` |

### 4.3 字体

当前 starter 没有引入品牌字体，使用浏览器 / Tailwind 默认 sans 栈，目的是减少模板初始依赖和字重加载成本。

规则：

- 标题和正文都走默认 sans
- 未来如果要建立品牌视觉，先在本文档中补字体方案，再落到代码

### 4.4 动效

当前只使用非常轻的状态过渡：

- `transition-colors`
- `transition-all`

约束：

- 不使用弹性 / 弹跳缓动
- 默认只做 hover、focus、theme toggle 级别的轻交互
- 如果后续加入更复杂的页面动效，先在本文档定义统一时长和缓动

## 5. 组件规范

### 5.1 `Button`

文件：`frontend/src/components/ui/button.tsx`

特点：

- 使用 `class-variance-authority`
- 支持 `asChild`
- 通过 `data-slot`、`data-variant`、`data-size` 暴露语义
- 当前内部自带 `cn()`，尚未提取到共享 `lib/utils.ts`

#### 已实现 variants

- `default`
- `destructive`
- `outline`
- `secondary`
- `ghost`
- `link`

#### 已实现 sizes

- `default`
- `xs`
- `sm`
- `lg`
- `icon`
- `icon-xs`
- `icon-sm`
- `icon-lg`

### 5.2 `ThemeToggle`

文件：`frontend/src/components/theme-toggle.tsx`

特点：

- 通过给 `document.documentElement` 添加 / 移除 `.dark` 切换主题
- 使用 `Moon` / `Sun` 图标表达状态
- 使用 `aria-label` 描述当前动作

限制：

- 当前状态不做本地持久化
- 只处理 class toggle，不处理系统主题侦测

## 6. 页面模式

### 6.1 Header

- `sticky top-0 z-50`
- 半透明背景 `bg-background/80`
- `backdrop-blur-sm`
- 内容区最大宽度 `max-w-5xl`

用途：

- 演示导航栏和主题切换的基础搭法

### 6.2 Hero

- 主体垂直水平居中
- 内容区 `max-w-2xl`
- 标题 `text-4xl sm:text-5xl`
- 副文案使用 `text-muted-foreground`
- CTA 使用按钮组并支持自动换行

### 6.3 Footer

- 极简单行文本
- 使用 `border-t`
- 使用 `text-sm text-muted-foreground`

## 7. 响应式规则

当前页面的响应式策略很轻：

- 小屏优先
- 主要依靠 `max-w-*` 控制阅读宽度
- 按钮组在窄屏下允许换行
- 标题仅在 `sm` 断点从 `text-4xl` 升到 `text-5xl`

没有 sidebar、复杂栅格或多断点编排，因此文档里不应虚构更复杂的布局体系。

## 8. 可访问性

当前 starter 需要保持这些基线：

- 所有可交互元素有可见 focus 样式
- 主题切换按钮有 `aria-label`
- 明暗主题均依赖语义 token，避免硬编码黑白
- 颜色不是唯一状态表达方式

## 9. 文件映射

```text
frontend/src/
├── app/App.tsx
├── components/theme-toggle.tsx
├── components/ui/button.tsx
├── main.tsx
├── styles/globals.css
└── test/setup.ts
```

## 10. 扩展规则

当项目从模板进入真实产品阶段：

1. 先在本文档补产品调性、字体和新的页面模式
2. 再扩展 token，不要直接在组件里塞硬编码
3. 当第二个以上共享组件需要 `cn()` 时，提取 `frontend/src/lib/utils.ts`
4. 当页面开始分领域增长时，再新增 `features/`、`hooks/`、`lib/`

## 11. 禁止事项

- 不要在文档里保留 `[待定]` 占位假装规范已完成
- 不要把未来规划写成当前实现
- 不要引入紫色渐变模板感 hero 来污染 starter
- 不要在没有品牌设计的情况下硬上复杂视觉语言
