import { useState } from 'react'
import './ReportGenerator.css'
import type { UploadedFileInfo } from '../App'

interface ReportGeneratorProps {
  uploadedFiles: UploadedFileInfo[]
  onClearFiles: () => void
}

interface Report {
  key_metrics?: Record<string, any>
  trends_and_correlations?: Record<string, string>
  recommendations?: Record<string, string> | string[]
  summary?: string
}

export default function ReportGenerator({ uploadedFiles, onClearFiles }: ReportGeneratorProps) {
  const [selectedFileIds, setSelectedFileIds] = useState<number[]>([])
  const [loadingAction, setLoadingAction] = useState<'json' | 'pdf' | null>(null)
  const [report, setReport] = useState<Report | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleToggleFile = (fileId: number) => {
    setSelectedFileIds(prev =>
      prev.includes(fileId)
        ? prev.filter(id => id !== fileId)
        : [...prev, fileId]
    )
  }

  const handleSelectAll = () => {
    if (selectedFileIds.length === uploadedFiles.length) {
      setSelectedFileIds([])
    } else {
      setSelectedFileIds(uploadedFiles.map(f => f.file_id))
    }
  }

  const handleGenerateJSON = async () => {
    if (selectedFileIds.length === 0) {
      setError('Please select at least one file')
      return
    }

    setLoadingAction('json')
    setError(null)
    setReport(null)

    try {
      const queryParams = selectedFileIds.map(id => `file_ids=${id}`).join('&')
      const response = await fetch(`/report/?${queryParams}`)

      if (!response.ok) {
        throw new Error('Failed to generate report')
      }

      const data = await response.json()
      setReport(data.report)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate report')
    } finally {
      setLoadingAction(null)
    }
  }

  const handleGeneratePDF = async () => {
    if (selectedFileIds.length === 0) {
      setError('Please select at least one file')
      return
    }

    setLoadingAction('pdf')
    setError(null)

    try {
      const queryParams = selectedFileIds.map(id => `file_ids=${id}`).join('&')
      const response = await fetch(`/report/pdf?${queryParams}`)

      if (!response.ok) {
        throw new Error('Failed to generate PDF')
      }

      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `report-${Date.now()}.pdf`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate PDF')
    } finally {
      setLoadingAction(null)
    }
  }

  const renderMetrics = (metrics: Record<string, any>) => {
    return (
      <div className="metrics-grid">
        {Object.entries(metrics).map(([key, value]) => (
          <div key={key} className="metric-card">
            <div className="metric-label">{key.replace(/_/g, ' ')}</div>
            <div className="metric-value">
              {typeof value === 'object' ? JSON.stringify(value, null, 2) : String(value)}
            </div>
          </div>
        ))}
      </div>
    )
  }

  const renderTrends = (trends: Record<string, string>) => {
    return (
      <ul className="trends-list">
        {Object.entries(trends).map(([key, value]) => (
          <li key={key}>
            <strong>{key.replace(/_/g, ' ')}:</strong> {value}
          </li>
        ))}
      </ul>
    )
  }

  const renderRecommendations = (recommendations: Record<string, string> | string[]) => {
    if (Array.isArray(recommendations)) {
      return (
        <ul className="recommendations-list">
          {recommendations.map((rec, idx) => (
            <li key={idx}>{rec}</li>
          ))}
        </ul>
      )
    }

    return (
      <ul className="recommendations-list">
        {Object.entries(recommendations).map(([key, value]) => (
          <li key={key}>
            <strong>{key.replace(/_/g, ' ')}:</strong> {value}
          </li>
        ))}
      </ul>
    )
  }

  return (
    <div className="report-generator-card">
      <div className="card-header">
        <h2>Generate Report</h2>
        <button onClick={onClearFiles} className="btn-secondary clear-btn">
          Clear All Files
        </button>
      </div>

      <div className="uploaded-files-section">
        <div className="section-header">
          <h3>Uploaded Files ({uploadedFiles.length})</h3>
          <button onClick={handleSelectAll} className="select-all-btn">
            {selectedFileIds.length === uploadedFiles.length ? 'Deselect All' : 'Select All'}
          </button>
        </div>

        <div className="files-grid">
          {uploadedFiles.map(file => (
            <div
              key={file.file_id}
              className={`file-card ${selectedFileIds.includes(file.file_id) ? 'selected' : ''}`}
              onClick={() => handleToggleFile(file.file_id)}
            >
              <input
                type="checkbox"
                checked={selectedFileIds.includes(file.file_id)}
                onChange={() => handleToggleFile(file.file_id)}
                onClick={e => e.stopPropagation()}
              />
              <div className="file-card-content">
                <span className="file-card-name">{file.filename}</span>
                <span className="file-card-id">ID: {file.file_id}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="action-buttons">
        <button
          onClick={handleGenerateJSON}
          disabled={loadingAction !== null || selectedFileIds.length === 0}
          className="btn-primary"
        >
          {loadingAction === 'json' ? (
            <>
              <span className="spinner"></span>
              Generating...
            </>
          ) : (
            <>
              <span>📄</span>
              Generate JSON Report
            </>
          )}
        </button>

        <button
          onClick={handleGeneratePDF}
          disabled={loadingAction !== null || selectedFileIds.length === 0}
          className="btn-success"
        >
          {loadingAction === 'pdf' ? (
            <>
              <span className="spinner"></span>
              Generating PDF...
            </>
          ) : (
            <>
              <span>📑</span>
              Download PDF Report
            </>
          )}
        </button>
      </div>

      {error && (
        <div className="error-message">
          <span>⚠️</span> {error}
        </div>
      )}

      {report && (
        <div className="report-display">
          <h3>📈 Generated Report</h3>

          {report.summary && (
            <section className="report-section">
              <h4>Executive Summary</h4>
              <p className="summary-text">{report.summary}</p>
            </section>
          )}

          {report.key_metrics && (
            <section className="report-section">
              <h4>Key Metrics</h4>
              {renderMetrics(report.key_metrics)}
            </section>
          )}

          {report.trends_and_correlations && (
            <section className="report-section">
              <h4>Trends & Correlations</h4>
              {renderTrends(report.trends_and_correlations)}
            </section>
          )}

          {report.recommendations && (
            <section className="report-section">
              <h4>Recommendations</h4>
              {renderRecommendations(report.recommendations)}
            </section>
          )}
        </div>
      )}
    </div>
  )
}
