# AI Report Generator - Frontend

A modern React + TypeScript frontend for the AI Report Generator application.

## Features

- 📁 **File Upload**: Drag-and-drop or browse to upload CSV files and images
- 📊 **Report Generation**: Generate analytical reports in JSON or PDF format
- 🎨 **Modern UI**: Clean, responsive design with smooth interactions
- ⚡ **Fast**: Built with Vite for lightning-fast development and builds

## Tech Stack

- **React 19** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Build tool and dev server
- **CSS3** - Modern styling

## Getting Started

### Prerequisites

- Node.js 18+ installed
- Backend API running on `http://localhost:8000`

### Installation

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (if not already done)
npm install
```

### Development

```bash
# Start the development server
npm run dev
```

The application will be available at `http://localhost:3000`

### Build for Production

```bash
# Create optimized production build
npm run build

# Preview the production build
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── FileUpload.tsx         # File upload component
│   │   ├── FileUpload.css
│   │   ├── ReportGenerator.tsx    # Report generation component
│   │   └── ReportGenerator.css
│   ├── App.tsx                     # Main application component
│   ├── App.css
│   ├── main.tsx                    # Application entry point
│   └── index.css                   # Global styles
├── index.html
├── vite.config.ts                  # Vite configuration with proxy
└── package.json
```

## API Integration

The frontend communicates with the FastAPI backend through a Vite proxy configured in `vite.config.ts`:

- **POST /upload/** - Upload CSV/image files
- **GET /report/?file_ids={ids}** - Generate JSON report
- **GET /report/pdf?file_ids={ids}** - Download PDF report

## Usage

1. **Upload Files**: Click the upload area or drag files to upload CSV or image files
2. **Select Files**: Choose which uploaded files to include in the report
3. **Generate Report**: 
   - Click "Generate JSON Report" to view the report in the browser
   - Click "Download PDF Report" to download a formatted PDF

## Features Breakdown

### File Upload Component
- Multi-file selection support
- File type validation (CSV, PNG, JPG, JPEG)
- Visual file list with size display
- Individual file removal
- Upload progress indicator

### Report Generator Component
- File selection with checkboxes
- Select/deselect all functionality
- JSON report display with formatted sections:
  - Executive Summary
  - Key Metrics (with cards)
  - Trends & Correlations
  - Recommendations
- PDF download functionality
- Error handling and loading states

## Customization

### Styling

The application uses CSS custom properties (variables) defined in `index.css`:

```css
--primary-color: #667eea;
--secondary-color: #764ba2;
--success-color: #28a745;
--danger-color: #dc3545;
```

Modify these to change the color scheme.

### API Endpoint

If your backend runs on a different port, update the proxy configuration in `vite.config.ts`:

```typescript
proxy: {
  '/upload': {
    target: 'http://localhost:YOUR_PORT',
    changeOrigin: true,
  },
  '/report': {
    target: 'http://localhost:YOUR_PORT',
    changeOrigin: true,
  }
}
```

## Troubleshooting

### CORS Errors

Ensure the backend has CORS enabled for `http://localhost:3000`. Check `app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Connection Refused

Make sure the backend is running on port 8000:

```bash
# In the project root directory
uvicorn app.main:app --reload --port 8000
```

## License

Part of the AI Report Generator project.
