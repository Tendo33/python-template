import { Button } from "@/components/ui/button"
import { ThemeToggle } from "@/components/theme-toggle"

export function App() {
  return (
    <div className="flex min-h-svh flex-col">
      <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur-sm">
        <div className="mx-auto flex h-14 max-w-5xl items-center justify-between px-4">
          <span className="text-lg font-semibold tracking-tight">
            Python Template
          </span>
          <ThemeToggle />
        </div>
      </header>

      <main className="flex flex-1 items-center justify-center px-4">
        <div className="mx-auto max-w-2xl text-center">
          <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
            Ready to build
          </h1>
          <p className="mt-4 text-lg text-muted-foreground">
            React + TypeScript + Vite + Tailwind CSS + shadcn/ui
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
            <Button size="lg" asChild>
              <a
                href="https://ui.shadcn.com"
                target="_blank"
                rel="noopener noreferrer"
              >
                shadcn/ui Docs
              </a>
            </Button>
            <Button variant="outline" size="lg" asChild>
              <a
                href="https://vite.dev"
                target="_blank"
                rel="noopener noreferrer"
              >
                Vite Docs
              </a>
            </Button>
          </div>
        </div>
      </main>

      <footer className="border-t border-border py-6 text-center text-sm text-muted-foreground">
        Built with pnpm + React + Vite + Tailwind + shadcn/ui
      </footer>
    </div>
  )
}
