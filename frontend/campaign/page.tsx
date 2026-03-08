"use client"

import { useState,useEffect } from "react"
import api from "@/lib/api"

export default function CampaignPage(){

  const [firmwareList,setFirmwareList] = useState<any[]>([])
  const [selectedFW,setSelectedFW] = useState("")
  const [batchSize,setBatchSize] = useState(10)
  const [status,setStatus] = useState("")

  useEffect(()=>{

    api.get("/firmware")
      .then(r => setFirmwareList(r.data))

  },[])

  const startCampaign = () => {

    api.post("/campaigns",{
      firmware_id: Number(selectedFW),
      batch_size: batchSize
    })

    .then(()=> setStatus("Campaign started successfully"))
    .catch(()=> setStatus("Error: Could not start campaign"))

  }

  return(

    <div className="p-6">

      <h1 className="text-2xl font-bold mb-4">
        Launch Update Campaign
      </h1>

      <div className="bg-white rounded-xl shadow p-6 max-w-md">

        <label className="block mb-2 font-medium">
          Firmware Version
        </label>

        <select
          className="w-full border rounded p-2 mb-4"
          onChange={(e)=> setSelectedFW(e.target.value)}
        >

          <option value="">
            -- Select --
          </option>

          {firmwareList.map(f =>(

            <option
              key={f.firmware_id}
              value={f.firmware_id}
            >
              {f.version}
            </option>

          ))}

        </select>

        <label className="block mb-2 font-medium">
          Initial Batch Size
        </label>

        <input
          type="number"
          value={batchSize}
          min={1}
          max={50}
          onChange={(e)=> setBatchSize(Number(e.target.value))}
          className="w-full border rounded p-2 mb-4"
        />

        <button
          onClick={startCampaign}
          className="w-full bg-blue-600 text-white py-2 rounded-lg font-semibold hover:bg-blue-700"
        >
          Start Campaign
        </button>

        {status && (
          <p className="mt-3 text-green-600">
            {status}
          </p>
        )}

      </div>

    </div>

  )

}