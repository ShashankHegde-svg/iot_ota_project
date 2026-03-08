"use client"

import { useEffect, useState } from "react"
import api from "@/lib/api"

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts"

export default function AnalyticsPage(){

  const [devices,setDevices] = useState<any[]>([])

  useEffect(()=>{

    api.get("/devices")
      .then(r => setDevices(r.data))

  },[])

  const total = devices.length
  const success = devices.filter(d => d.status === "success").length
  const failed = devices.filter(d => d.status === "failed").length
  const idle = devices.filter(d => d.status === "idle").length

  const chartData = [
    { name:"Success", count:success, fill:"#22c55e"},
    { name:"Failed", count:failed, fill:"#ef4444"},
    { name:"Idle", count:idle, fill:"#94a3b8"}
  ]

  return(

    <div className="p-6">

      <h1 className="text-2xl font-bold mb-6">
        Analytics
      </h1>

      {/* Stats Boxes */}

      <div className="grid grid-cols-3 gap-4 mb-8">

        <div className="bg-green-50 border border-green-200 rounded-xl p-4 text-center">
          <p className="text-3xl font-bold text-green-600">{success}</p>
          <p className="text-sm text-green-700">Successful</p>
        </div>

        <div className="bg-red-50 border border-red-200 rounded-xl p-4 text-center">
          <p className="text-3xl font-bold text-red-600">{failed}</p>
          <p className="text-sm text-red-700">Failed</p>
        </div>

        <div className="bg-gray-50 border border-gray-200 rounded-xl p-4 text-center">
          <p className="text-3xl font-bold text-gray-700">{total}</p>
          <p className="text-sm text-gray-600">Total Devices</p>
        </div>

      </div>

      {/* Chart */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-lg font-semibold mb-4">
          Device Status Breakdown
        </h2>

        <ResponsiveContainer width="100%" height={300}>

          <BarChart data={chartData}>

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar dataKey="count" fill="#3b82f6" />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>

  )

}