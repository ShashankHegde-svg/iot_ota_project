import "./globals.css"
import Link from "next/link"

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {

  return (

    <html lang="en">

      <body className="flex min-h-screen">

        {/* Sidebar */}

        <nav className="w-52 bg-slate-800 text-white p-4 flex flex-col gap-2">

          <h2 className="text-xl font-bold mb-4">
            OTA Manager
          </h2>

          <Link
            href="/"
            className="p-2 rounded hover:bg-slate-700"
          >
            Fleet
          </Link>

          <Link
            href="/campaign"
            className="p-2 rounded hover:bg-slate-700"
          >
            Campaigns
          </Link>

          <Link
            href="/analytics"
            className="p-2 rounded hover:bg-slate-700"
          >
            Analytics
          </Link>

        </nav>

        {/* Page Content */}

        <main className="flex-1 bg-gray-50">
          {children}
        </main>

      </body>

    </html>

  )

}