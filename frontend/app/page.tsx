"use client"

import { useEffect, useState } from "react"
import api from "@/lib/api"

type Device = {
  device_id: string
  firmware_version: string
  battery_level: number
  network_quality: number
  status: string
}

const statusColor: Record<string,string> = {
  idle: "bg-gray-100 border-gray-300 text-gray-600",
  updating: "bg-blue-100 border-blue-400 text-blue-700",
  downloading: "bg-yellow-100 border-yellow-400 text-yellow-700",
  success: "bg-green-100 border-green-400 text-green-700",
  failed: "bg-red-100 border-red-400 text-red-700"
}

export default function Home(){

  const [devices,setDevices] = useState<Device[]>([])

  useEffect(()=>{

    const fetch = () =>
      api.get("/devices")
        .then(r => setDevices(r.data))

    fetch()

    const interval = setInterval(fetch,3000)

    return ()=> clearInterval(interval)

  },[])

  return(

    <main className="p-6 bg-gray-50 min-h-screen">

      <h1 className="text-3xl font-bold text-gray-800 mb-2">
        OTA Fleet Dashboard
      </h1>

      <p className="text-gray-500 mb-6">
        {devices.length} devices connected
      </p>

      <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3">

        {devices.map(d =>(

          <div
            key={d.device_id}
            className={`border-2 rounded-lg p-3 ${statusColor[d.status]}`}
          >

            <p className="text-xs font-bold">
              {d.device_id}
            </p>

            <p className="text-xs">
              FW: {d.firmware_version}
            </p>

            <p className="text-xs">
              Bat: {d.battery_level}%
            </p>

            <p className="text-xs capitalize font-semibold mt-1">
              {d.status}
            </p>

          </div>

        ))}

      </div>

    </main>
  )
}