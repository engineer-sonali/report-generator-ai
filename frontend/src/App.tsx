import { useState } from 'react'
import './App.css'
import FileUpload from './components/FileUpload'
import ReportGenerator from './components/ReportGenerator'

export interface UploadedFileInfo {
  file_id: number
  filename: string
  vector_id: string
}

function App() {
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFileInfo[]>([])

  const handleFilesUploaded = (files: UploadedFileInfo[]) => {
    setUploadedFiles(prev => [...prev, ...files])
  }

  const handleClearFiles = () => {
    setUploadedFiles([])
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🤖 AI Report Generator</h1>
        <p>Upload CSV files and images to generate intelligent business analytics reports</p>
      </header>

      <main className="app-main">
        <FileUpload onFilesUploaded={handleFilesUploaded} />
        
        {uploadedFiles.length > 0 && (
          <ReportGenerator 
            uploadedFiles={uploadedFiles} 
            onClearFiles={handleClearFiles}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>Powered by FastAPI, OpenAI, and Qdrant Vector Database</p>
      </footer>
    </div>
  )
}

export default App
