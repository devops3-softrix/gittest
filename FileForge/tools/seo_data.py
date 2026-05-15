"""
SEO metadata and related-tools mapping for all 42 conversion tools.

Each key is the URL name (matching the urlpatterns name= parameter).
"""

TOOL_SEO = {
    # ── PDF Tools ─────────────────────────────────────────────────────────
    "pdf_to_docx": {
        "seo_title": "PDF to DOCX Converter — Convert PDF to Editable Word | FileForge",
        "seo_description": "Convert PDF files to editable Word DOCX documents online. Preserves formatting, tables, and images. Free, fast, and secure.",
        "long_description": (
            "Our PDF to DOCX converter transforms your PDF files into fully editable Microsoft Word documents. "
            "Unlike simple text extraction, this tool preserves the original layout including tables, images, and formatting — "
            "making it easy to edit contracts, reports, and academic papers without retyping.\n\n"
            "The conversion runs entirely on our server using advanced Python-based parsing. "
            "Your files are processed instantly and never stored permanently."
        ),
        "use_cases": [
            "Edit text in a PDF contract or agreement",
            "Update an old report that only exists as a PDF",
            "Extract formatted content from scanned documents",
            "Modify academic papers or research documents",
        ],
        "related_tools": ["pdf_to_txt", "pdf_to_odt", "pdf_to_pptx", "docx_to_pdf"],
    },
    "pdf_to_txt": {
        "seo_title": "PDF to TXT — Extract Text from PDF | FileForge",
        "seo_description": "Extract all text content from PDF files into plain TXT format. Fast, free, and no sign-up required for your first conversions.",
        "long_description": (
            "Quickly extract all readable text from any PDF document into a clean plain-text file. "
            "Perfect for indexing, searching, or processing PDF content programmatically.\n\n"
            "The tool reads every page of your PDF and outputs the text in reading order, "
            "separated by page breaks. Ideal for data processing pipelines and content analysis."
        ),
        "use_cases": [
            "Extract text for search indexing or NLP processing",
            "Copy content from a PDF without formatting issues",
            "Create accessible plain-text versions of documents",
            "Feed PDF content into AI or analysis tools",
        ],
        "related_tools": ["pdf_to_docx", "pdf_to_csv", "pdf_to_xlsx", "pdf_to_odt"],
    },
    "pdf_to_png": {
        "seo_title": "PDF to PNG — Convert PDF Pages to PNG Images | FileForge",
        "seo_description": "Convert each page of a PDF into high-resolution PNG images. Download as a ZIP archive. Fast and secure.",
        "long_description": (
            "Transform every page of your PDF into crystal-clear PNG images at 2x resolution. "
            "Each page becomes a separate PNG file, delivered as a convenient ZIP archive.\n\n"
            "PNG format preserves sharp text and graphics with lossless compression — ideal "
            "for presentations, web content, and social media where image quality matters."
        ),
        "use_cases": [
            "Create slide images from a PDF presentation",
            "Embed PDF pages in a website or blog post",
            "Share individual pages on social media",
            "Create thumbnails for document previews",
        ],
        "related_tools": ["pdf_to_jpg", "pdf_to_bmp", "pdf_to_tiff", "pdf_to_svg"],
    },
    "pdf_to_jpg": {
        "seo_title": "PDF to JPG — Convert PDF Pages to JPEG Images | FileForge",
        "seo_description": "Convert PDF pages to JPEG images with high quality. Each page as a separate JPG, delivered in a ZIP.",
        "long_description": (
            "Convert your PDF document into JPEG images — one per page. JPG is the most widely "
            "supported image format, making it perfect for sharing, uploading, and embedding.\n\n"
            "Our converter renders each page at 2x resolution for sharp, professional results "
            "while keeping file sizes manageable thanks to JPEG compression."
        ),
        "use_cases": [
            "Upload PDF pages to platforms that only accept images",
            "Create lightweight image versions for email attachments",
            "Preview documents in image galleries",
            "Convert scanned documents to shareable images",
        ],
        "related_tools": ["pdf_to_png", "pdf_to_bmp", "pdf_to_tiff", "pdf_to_svg"],
    },
    "pdf_to_bmp": {
        "seo_title": "PDF to BMP — Convert PDF Pages to Bitmap Images | FileForge",
        "seo_description": "Convert PDF pages to uncompressed BMP bitmap images. Lossless quality for every page.",
        "long_description": (
            "Convert PDF pages to BMP (Bitmap) format — an uncompressed image format that preserves "
            "every pixel without compression artifacts. Best for workflows that require raw image data.\n\n"
            "Each page is rendered at high resolution and saved as a separate BMP file in a ZIP archive."
        ),
        "use_cases": [
            "Print shops requiring uncompressed image input",
            "Legacy software that only accepts BMP format",
            "High-fidelity archival of document pages",
        ],
        "related_tools": ["pdf_to_png", "pdf_to_jpg", "pdf_to_tiff", "pdf_to_ppm"],
    },
    "pdf_to_tiff": {
        "seo_title": "PDF to TIFF — Convert PDF to TIFF Images | FileForge",
        "seo_description": "Convert PDF documents to TIFF image format. Professional-grade lossless quality for archival and printing.",
        "long_description": (
            "Convert your PDF pages to TIFF (Tagged Image File Format) — the industry standard "
            "for archival and professional printing. TIFF preserves full image quality without compression loss.\n\n"
            "Ideal for legal, medical, and financial document archiving where quality is non-negotiable."
        ),
        "use_cases": [
            "Archive legal or medical documents as images",
            "Submit documents to systems requiring TIFF input",
            "Professional print production workflows",
        ],
        "related_tools": ["pdf_to_png", "pdf_to_bmp", "pdf_to_jpg", "pdf_to_ppm"],
    },
    "pdf_to_ppm": {
        "seo_title": "PDF to PPM — Convert PDF Pages to PPM Format | FileForge",
        "seo_description": "Convert PDF pages to PPM (Portable Pixmap) image format. Useful for image processing pipelines.",
        "long_description": (
            "Convert PDF pages to PPM (Portable Pixmap) format — a simple, uncompressed image format "
            "commonly used in Unix/Linux image processing pipelines and scientific computing.\n\n"
            "PPM files are easy to read programmatically, making this tool ideal for developers and researchers."
        ),
        "use_cases": [
            "Feed PDF pages into image processing scripts",
            "Use with Unix/Linux command-line image tools",
            "Scientific image analysis workflows",
        ],
        "related_tools": ["pdf_to_png", "pdf_to_bmp", "pdf_to_tiff", "pdf_to_svg"],
    },
    "pdf_to_svg": {
        "seo_title": "PDF to SVG — Convert PDF Pages to Vector SVG | FileForge",
        "seo_description": "Convert PDF pages to scalable SVG vector graphics. Perfect for web use and infinite zoom without quality loss.",
        "long_description": (
            "Transform PDF pages into SVG (Scalable Vector Graphics) — a vector format that scales "
            "to any size without losing quality. Perfect for embedding in websites, presentations, and responsive designs.\n\n"
            "SVG files are resolution-independent, meaning they look sharp on Retina displays, 4K screens, "
            "and printed materials alike."
        ),
        "use_cases": [
            "Embed PDF diagrams in websites as scalable graphics",
            "Create resolution-independent document previews",
            "Use PDF illustrations in design tools like Figma or Illustrator",
        ],
        "related_tools": ["pdf_to_png", "pdf_to_jpg", "pdf_to_pptx", "pdf_to_docx"],
    },
    "pdf_to_pptx": {
        "seo_title": "PDF to PowerPoint — Convert PDF to PPTX Slides | FileForge",
        "seo_description": "Convert PDF documents to PowerPoint PPTX presentations. Each page becomes an editable slide.",
        "long_description": (
            "Turn any PDF into a PowerPoint presentation — each PDF page becomes a slide with the content "
            "rendered as a high-resolution image. Great for reusing PDF content in presentations.\n\n"
            "The tool preserves the visual layout perfectly by embedding each page as a full-slide image, "
            "so charts, diagrams, and complex layouts come through exactly as they appear in the PDF."
        ),
        "use_cases": [
            "Reuse PDF report content in a presentation",
            "Convert PDF slides back to editable PowerPoint format",
            "Create a slide deck from a PDF brochure or catalog",
        ],
        "related_tools": ["pdf_to_docx", "pdf_to_png", "pptx_to_pdf", "docx_to_pptx"],
    },
    "pdf_to_xlsx": {
        "seo_title": "PDF to Excel — Extract PDF Content to XLSX Spreadsheet | FileForge",
        "seo_description": "Extract text content from PDF files into Excel XLSX spreadsheets with one row per page.",
        "long_description": (
            "Extract the text content from each page of your PDF into an Excel spreadsheet. "
            "Each page becomes a row with its text content, making it easy to search, filter, and analyze.\n\n"
            "Ideal for processing multi-page reports, invoices, or data sheets where you need "
            "the content in a structured, editable format."
        ),
        "use_cases": [
            "Extract tabular data from PDF reports",
            "Create searchable spreadsheets from PDF archives",
            "Process invoice or receipt data in Excel",
        ],
        "related_tools": ["pdf_to_csv", "pdf_to_txt", "xlsx_to_pdf", "xlsx_to_csv"],
    },
    "pdf_to_csv": {
        "seo_title": "PDF to CSV — Extract PDF Text to CSV | FileForge",
        "seo_description": "Extract text from PDF files into CSV format with page numbers. Easy to import into any spreadsheet or database.",
        "long_description": (
            "Convert your PDF text content into a clean CSV file with page numbers and text columns. "
            "CSV is universally supported — import it into Excel, Google Sheets, databases, or analysis tools.\n\n"
            "Each page of your PDF becomes a row in the CSV, making it simple to process and analyze document content."
        ),
        "use_cases": [
            "Import PDF text into databases or data pipelines",
            "Create structured datasets from PDF documents",
            "Feed document content into data analysis tools",
        ],
        "related_tools": ["pdf_to_xlsx", "pdf_to_txt", "csv_to_xlsx", "xlsx_to_csv"],
    },
    "pdf_to_odt": {
        "seo_title": "PDF to ODT — Convert PDF to OpenDocument Text | FileForge",
        "seo_description": "Convert PDF files to OpenDocument Text (ODT) format for editing in LibreOffice and OpenOffice.",
        "long_description": (
            "Convert your PDF documents to ODT (OpenDocument Text) format — the open standard for word processing "
            "used by LibreOffice, OpenOffice, and other free office suites.\n\n"
            "ODT is an open, vendor-neutral format, making it ideal for organizations that prefer "
            "open-source software and long-term document archiving."
        ),
        "use_cases": [
            "Edit PDF documents in LibreOffice Writer",
            "Convert proprietary PDFs to open-format documents",
            "Archive documents in a vendor-neutral format",
        ],
        "related_tools": ["pdf_to_docx", "pdf_to_txt", "docx_to_odt", "pdf_to_pptx"],
    },
    "pdf_to_zip": {
        "seo_title": "PDF to ZIP — Package PDF in a ZIP Archive | FileForge",
        "seo_description": "Wrap your PDF file inside a ZIP archive for smaller file size and easier sharing.",
        "long_description": (
            "Package your PDF file inside a ZIP archive. ZIP compression can reduce file size and "
            "makes it easier to share files via email or file-sharing services that prefer archived formats.\n\n"
            "The original PDF is preserved exactly as-is inside the archive."
        ),
        "use_cases": [
            "Compress large PDFs for email attachments",
            "Package documents for upload to portals requiring ZIP",
            "Organize multiple related files into an archive",
        ],
        "related_tools": ["pdf_split", "pdf_merge", "pdf_encrypt"],
    },
    "pdf_split": {
        "seo_title": "Split PDF — Split PDF into Individual Pages | FileForge",
        "seo_description": "Split a multi-page PDF into individual single-page PDF files. Download as a ZIP archive.",
        "long_description": (
            "Split any multi-page PDF into individual single-page PDF files. Each page becomes its own "
            "standalone PDF document, all packaged in a convenient ZIP download.\n\n"
            "Perfect for extracting specific pages from a large document, distributing individual pages "
            "to different recipients, or reorganizing document content."
        ),
        "use_cases": [
            "Extract specific pages from a large document",
            "Send individual pages to different collaborators",
            "Break up a PDF for separate processing or review",
        ],
        "related_tools": ["pdf_merge", "pdf_encrypt", "pdf_to_png", "pdf_to_zip"],
    },
    "pdf_merge": {
        "seo_title": "Merge PDFs — Combine Multiple PDFs into One | FileForge",
        "seo_description": "Merge and combine multiple PDF files into a single document. Upload your PDFs and get one merged file.",
        "long_description": (
            "Combine two or more PDF files into a single, unified document. Simply upload all your PDFs — "
            "they'll be merged in the order you select.\n\n"
            "Ideal for combining report sections, assembling portfolios, or creating comprehensive "
            "documents from multiple sources."
        ),
        "use_cases": [
            "Combine separate report chapters into one PDF",
            "Merge scanned document pages into a single file",
            "Assemble a portfolio from multiple PDF sources",
            "Combine cover letter and resume into one document",
        ],
        "related_tools": ["pdf_split", "pdf_encrypt", "pdf_to_zip"],
    },
    "pdf_encrypt": {
        "seo_title": "Encrypt PDF — Password-Protect Your PDF | FileForge",
        "seo_description": "Add AES password protection to your PDF files. Secure sensitive documents with encryption.",
        "long_description": (
            "Protect your sensitive PDF documents with AES encryption. Set a password that must be entered "
            "before anyone can view the document contents.\n\n"
            "Ideal for confidential business documents, financial records, legal contracts, and any "
            "file you need to share securely."
        ),
        "use_cases": [
            "Protect confidential contracts before sharing",
            "Secure financial statements and tax documents",
            "Add password protection to legal filings",
            "Encrypt personal documents for cloud storage",
        ],
        "related_tools": ["pdf_merge", "pdf_split", "pdf_to_zip"],
    },

    # ── DOCX Tools ────────────────────────────────────────────────────────
    "docx_to_pdf": {
        "seo_title": "DOCX to PDF — Convert Word to PDF | FileForge",
        "seo_description": "Convert Microsoft Word DOCX files to PDF format. Preserves formatting, fonts, and layout.",
        "long_description": (
            "Convert your Microsoft Word documents to universally readable PDF format. "
            "The conversion preserves headings, paragraphs, tables, and basic formatting so your document "
            "looks professional in any PDF viewer.\n\n"
            "PDF is the standard format for sharing finalized documents — no one can accidentally edit your content."
        ),
        "use_cases": [
            "Share a finalized report or proposal as PDF",
            "Submit assignments or applications in PDF format",
            "Create print-ready versions of Word documents",
            "Archive documents in a universally readable format",
        ],
        "related_tools": ["pdf_to_docx", "docx_to_txt", "docx_to_odt", "docx_to_pptx"],
    },
    "docx_to_txt": {
        "seo_title": "DOCX to TXT — Extract Text from Word Documents | FileForge",
        "seo_description": "Extract plain text from Microsoft Word DOCX files. Strip formatting and get clean text output.",
        "long_description": (
            "Strip all formatting from a Word document and extract just the plain text content. "
            "Perfect for content migration, text analysis, or when you need just the words without any styling.\n\n"
            "Headings, paragraphs, and list items are all extracted and separated by line breaks."
        ),
        "use_cases": [
            "Extract content for text analysis or NLP",
            "Create plain-text versions of formatted documents",
            "Migrate content between different systems",
        ],
        "related_tools": ["docx_to_pdf", "docx_to_odt", "pdf_to_txt"],
    },
    "docx_to_odt": {
        "seo_title": "DOCX to ODT — Convert Word to OpenDocument | FileForge",
        "seo_description": "Convert Microsoft Word DOCX files to OpenDocument Text (ODT) format for LibreOffice.",
        "long_description": (
            "Convert Word documents to OpenDocument Text format, the open standard used by LibreOffice, "
            "OpenOffice, and other free office suites. Preserves headings, paragraphs, and document structure.\n\n"
            "ODT is ideal for cross-platform compatibility and organizations committed to open-source software."
        ),
        "use_cases": [
            "Open Word files in LibreOffice without compatibility issues",
            "Convert to open standards for archival compliance",
            "Share documents with users who don't have Microsoft Office",
        ],
        "related_tools": ["docx_to_pdf", "docx_to_txt", "pdf_to_odt", "docx_to_pptx"],
    },
    "docx_to_pptx": {
        "seo_title": "DOCX to PPTX — Convert Word to PowerPoint | FileForge",
        "seo_description": "Convert Word document headings and content into PowerPoint slides automatically.",
        "long_description": (
            "Transform your Word document into a PowerPoint presentation automatically. "
            "Each heading in your document becomes a slide title, and the paragraphs beneath it become slide bullets.\n\n"
            "Great for quickly turning written content into presentation format without manual copy-pasting."
        ),
        "use_cases": [
            "Turn a written report into a presentation",
            "Create slides from meeting notes or outlines",
            "Convert documentation into training presentations",
        ],
        "related_tools": ["docx_to_pdf", "pdf_to_pptx", "pptx_to_pdf"],
    },
    "docx_to_png": {
        "seo_title": "DOCX to PNG — Convert Word Pages to PNG Images | FileForge",
        "seo_description": "Convert each page of a Word document into high-quality PNG images. Download as a ZIP.",
        "long_description": (
            "Render each page of your Word document as a high-resolution PNG image. "
            "The document is first converted to PDF internally, then each page is rendered at 2x resolution.\n\n"
            "Perfect for creating image previews of documents or sharing pages on platforms that only accept images."
        ),
        "use_cases": [
            "Create document previews for websites or apps",
            "Share document pages on social media or chat",
            "Generate thumbnails for document management systems",
        ],
        "related_tools": ["docx_to_jpg", "docx_to_pdf", "pdf_to_png"],
    },
    "docx_to_jpg": {
        "seo_title": "DOCX to JPG — Convert Word Pages to JPEG Images | FileForge",
        "seo_description": "Convert Word document pages to JPEG images. Lightweight and widely supported.",
        "long_description": (
            "Convert each page of your Word document into a JPEG image. JPEG offers excellent compression "
            "for smaller file sizes while maintaining good visual quality.\n\n"
            "Ideal for sharing document pages via email, messaging apps, or platforms with image upload limits."
        ),
        "use_cases": [
            "Create lightweight image versions for email sharing",
            "Upload document pages to image-only platforms",
            "Generate compact previews of Word documents",
        ],
        "related_tools": ["docx_to_png", "docx_to_pdf", "pdf_to_jpg"],
    },

    # ── Image Tools ───────────────────────────────────────────────────────
    "to_jpg": {
        "seo_title": "Image to JPG — Convert Any Image to JPEG | FileForge",
        "seo_description": "Convert PNG, BMP, TIFF, WebP, HEIC and other image formats to JPEG. Fast and free.",
        "long_description": (
            "Convert any image format — PNG, BMP, TIFF, WebP, HEIC, and more — to the universally "
            "supported JPEG format. JPEG is the most widely compatible image format for web, email, and social media.\n\n"
            "The converter automatically handles color mode conversions and produces optimized output."
        ),
        "use_cases": [
            "Convert iPhone HEIC photos to JPEG for sharing",
            "Reduce PNG file sizes by converting to JPEG",
            "Prepare images for web upload or email",
        ],
        "related_tools": ["to_png", "to_webp", "to_bmp", "to_tiff"],
    },
    "to_png": {
        "seo_title": "Image to PNG — Convert Any Image to PNG | FileForge",
        "seo_description": "Convert JPEG, BMP, TIFF, WebP, HEIC images to PNG format with lossless quality.",
        "long_description": (
            "Convert any image to PNG (Portable Network Graphics) — a lossless format that preserves "
            "every detail including transparency. Ideal for graphics, screenshots, and images where quality is paramount.\n\n"
            "PNG supports alpha transparency, making it perfect for logos, icons, and overlay graphics."
        ),
        "use_cases": [
            "Convert photos to PNG for lossless editing",
            "Create transparent-background versions of images",
            "Prepare images for graphic design projects",
        ],
        "related_tools": ["to_jpg", "to_webp", "to_bmp", "to_tiff"],
    },
    "to_bmp": {
        "seo_title": "Image to BMP — Convert Any Image to Bitmap | FileForge",
        "seo_description": "Convert images to BMP (Bitmap) format. Uncompressed, lossless image conversion.",
        "long_description": (
            "Convert any image to BMP (Bitmap) format — an uncompressed image format that stores every pixel "
            "without any compression. BMP files are large but preserve absolute fidelity.\n\n"
            "Used primarily with legacy Windows applications and systems that require raw bitmap data."
        ),
        "use_cases": [
            "Prepare images for legacy software requiring BMP",
            "Create uncompressed versions for pixel-level editing",
            "Compatibility with older Windows applications",
        ],
        "related_tools": ["to_png", "to_jpg", "to_tiff", "to_webp"],
    },
    "to_tiff": {
        "seo_title": "Image to TIFF — Convert Any Image to TIFF | FileForge",
        "seo_description": "Convert images to TIFF format. Professional-grade quality for print and archival.",
        "long_description": (
            "Convert any image to TIFF (Tagged Image File Format) — the professional standard for "
            "high-quality image storage used in publishing, printing, and medical imaging.\n\n"
            "TIFF supports multiple color spaces and is the preferred format for professional photographers and publishers."
        ),
        "use_cases": [
            "Prepare images for professional printing",
            "Archive photos in museum-grade quality",
            "Submit images to publishers or print shops",
        ],
        "related_tools": ["to_png", "to_jpg", "to_bmp", "to_webp"],
    },
    "to_webp": {
        "seo_title": "Image to WebP — Convert Any Image to WebP | FileForge",
        "seo_description": "Convert images to modern WebP format. Smaller file sizes with excellent quality for web use.",
        "long_description": (
            "Convert any image to WebP — Google's modern image format that offers superior compression "
            "compared to JPEG and PNG. WebP typically produces files 25-35% smaller with equivalent quality.\n\n"
            "WebP is supported by all major browsers and is the recommended format for web performance optimization."
        ),
        "use_cases": [
            "Optimize images for faster website loading",
            "Reduce image bandwidth for web applications",
            "Convert photo libraries to a more efficient format",
        ],
        "related_tools": ["to_jpg", "to_png", "to_heic", "to_tiff"],
    },
    "to_heic": {
        "seo_title": "Image to HEIC — Convert Any Image to Apple HEIC | FileForge",
        "seo_description": "Convert images to HEIC (HEIF) format. Apple's efficient image format with excellent quality.",
        "long_description": (
            "Convert any image to HEIC (High Efficiency Image Container) — Apple's default photo format "
            "that offers excellent quality at roughly half the file size of JPEG.\n\n"
            "HEIC is natively supported on iOS, macOS, and increasingly on other platforms."
        ),
        "use_cases": [
            "Convert images for Apple device compatibility",
            "Reduce photo storage with efficient HEIC compression",
            "Prepare images for iOS app development",
        ],
        "related_tools": ["to_jpg", "to_png", "to_webp"],
    },

    # ── Audio Tools ───────────────────────────────────────────────────────
    "m4a_to_mp3": {
        "seo_title": "M4A to MP3 — Convert Apple Audio to MP3 | FileForge",
        "seo_description": "Convert Apple M4A audio files to universally compatible MP3 format. High-quality conversion.",
        "long_description": (
            "Convert Apple M4A audio files to the universally compatible MP3 format. "
            "MP3 is supported by virtually every device, app, and platform — making it the safest choice for sharing.\n\n"
            "The conversion uses high-quality encoding settings to preserve audio fidelity."
        ),
        "use_cases": [
            "Share Apple voice memos with Android users",
            "Upload audio to platforms that only accept MP3",
            "Convert iTunes purchases for universal playback",
        ],
        "related_tools": ["mp3_to_wav", "mp4_to_mp3", "mp3_to_m4r"],
    },
    "mp3_to_wav": {
        "seo_title": "MP3 to WAV — Convert MP3 to Uncompressed Audio | FileForge",
        "seo_description": "Convert MP3 audio files to uncompressed WAV format for professional editing and production.",
        "long_description": (
            "Convert compressed MP3 audio to uncompressed WAV format. WAV files preserve full audio "
            "fidelity and are the standard input format for professional audio editing software.\n\n"
            "Essential for audio production, podcast editing, and any workflow requiring lossless audio."
        ),
        "use_cases": [
            "Prepare audio files for professional editing in DAWs",
            "Convert music files for CD burning",
            "Import audio into video editing software",
        ],
        "related_tools": ["m4a_to_mp3", "mp4_to_wav", "mp3_to_m4r"],
    },
    "mp3_to_m4r": {
        "seo_title": "MP3 to M4R — Create iPhone Ringtones | FileForge",
        "seo_description": "Convert MP3 files to iPhone ringtone format (M4R). Automatically trimmed to 30 seconds.",
        "long_description": (
            "Create custom iPhone ringtones from any MP3 file. The converter automatically trims your audio "
            "to 30 seconds (Apple's maximum) and converts it to the M4R format required by iOS.\n\n"
            "After downloading, transfer the M4R file to your iPhone via iTunes or Finder to use it as a ringtone."
        ),
        "use_cases": [
            "Create custom iPhone ringtones from your music",
            "Convert podcast clips into notification sounds",
            "Make alert tones from sound effects",
        ],
        "related_tools": ["m4a_to_mp3", "mp3_to_wav", "mp4_to_mp3"],
    },
    "mp4_to_mp3": {
        "seo_title": "MP4 to MP3 — Extract Audio from Video | FileForge",
        "seo_description": "Extract the audio track from MP4 video files and save as MP3. Perfect for music and podcasts.",
        "long_description": (
            "Extract just the audio track from any MP4 video file and save it as an MP3. "
            "Perfect for saving music from video files, creating podcast versions of video content, "
            "or extracting voiceovers from presentations.\n\n"
            "The video stream is discarded — you get a clean, lightweight audio file."
        ),
        "use_cases": [
            "Save music from music videos as MP3",
            "Create audio-only versions of video podcasts",
            "Extract narration from recorded presentations",
        ],
        "related_tools": ["mp4_to_wav", "m4a_to_mp3", "mp3_to_wav"],
    },
    "mp4_to_wav": {
        "seo_title": "MP4 to WAV — Extract Audio from Video as WAV | FileForge",
        "seo_description": "Extract audio from MP4 video files as uncompressed WAV. Professional quality for editing.",
        "long_description": (
            "Extract the audio track from an MP4 video and save it as uncompressed WAV. "
            "WAV preserves full audio quality — ideal for professional editing, mixing, and mastering.\n\n"
            "Use this when you need the highest possible audio quality from a video source."
        ),
        "use_cases": [
            "Extract dialogue from video for audio editing",
            "Create high-quality samples from video content",
            "Prepare audio for professional mixing and mastering",
        ],
        "related_tools": ["mp4_to_mp3", "mp3_to_wav", "m4a_to_mp3"],
    },

    # ── Video Tools ───────────────────────────────────────────────────────
    "mp4_to_mov": {
        "seo_title": "MP4 to MOV — Convert MP4 to Apple QuickTime | FileForge",
        "seo_description": "Convert MP4 video files to Apple QuickTime MOV format. Compatible with Final Cut Pro and macOS.",
        "long_description": (
            "Convert MP4 videos to Apple QuickTime MOV format. MOV is the preferred format for macOS, "
            "Final Cut Pro, and Apple's professional video editing ecosystem.\n\n"
            "The conversion re-encodes audio and video for optimal compatibility with Apple software."
        ),
        "use_cases": [
            "Prepare videos for editing in Final Cut Pro",
            "Convert for Apple-native video playback",
            "Compatibility with macOS video workflows",
        ],
        "related_tools": ["mp4_to_webm", "mp4_to_avi", "mp4_to_mkv", "any_to_mp4"],
    },
    "mp4_to_webm": {
        "seo_title": "MP4 to WebM — Convert Video for the Web | FileForge",
        "seo_description": "Convert MP4 videos to open WebM format for web embedding with VP9 and Opus codecs.",
        "long_description": (
            "Convert MP4 to WebM — the open, royalty-free video format designed for the web. "
            "WebM uses VP9 video and Opus audio codecs for excellent quality at smaller file sizes.\n\n"
            "WebM is supported by all major browsers and is ideal for HTML5 video embedding."
        ),
        "use_cases": [
            "Embed videos on websites with HTML5 video tags",
            "Reduce video bandwidth for web delivery",
            "Create web-optimized versions of promotional videos",
        ],
        "related_tools": ["mp4_to_mov", "mp4_to_avi", "mp4_to_mkv", "any_to_mp4"],
    },
    "mp4_to_avi": {
        "seo_title": "MP4 to AVI — Convert MP4 to AVI Format | FileForge",
        "seo_description": "Convert MP4 video files to AVI format. Widely supported by Windows media players.",
        "long_description": (
            "Convert MP4 videos to AVI (Audio Video Interleave) — a classic video format with broad "
            "compatibility across Windows media players and legacy video software.\n\n"
            "AVI is particularly useful for older systems and applications that don't support modern codecs."
        ),
        "use_cases": [
            "Play videos on older Windows systems",
            "Compatibility with legacy video editing software",
            "Convert for DVD authoring workflows",
        ],
        "related_tools": ["mp4_to_mov", "mp4_to_wmv", "mp4_to_mkv", "any_to_mp4"],
    },
    "mp4_to_wmv": {
        "seo_title": "MP4 to WMV — Convert to Windows Media Video | FileForge",
        "seo_description": "Convert MP4 to Windows Media Video (WMV) format for Windows Media Player compatibility.",
        "long_description": (
            "Convert MP4 videos to WMV (Windows Media Video) — Microsoft's native video format. "
            "WMV is optimized for Windows Media Player and Microsoft's media ecosystem.\n\n"
            "Useful for presentations, streaming, and Windows-centric workflows."
        ),
        "use_cases": [
            "Prepare videos for Windows Media Player",
            "Create videos for PowerPoint presentations",
            "Compatibility with Microsoft-based systems",
        ],
        "related_tools": ["mp4_to_avi", "mp4_to_mov", "mp4_to_mkv", "any_to_mp4"],
    },
    "mp4_to_mkv": {
        "seo_title": "MP4 to MKV — Convert to Matroska Container | FileForge",
        "seo_description": "Convert MP4 videos to MKV (Matroska) format. Supports multiple tracks and subtitles.",
        "long_description": (
            "Convert MP4 videos to MKV (Matroska) — a flexible, open container format that supports "
            "multiple audio tracks, subtitles, and chapters within a single file.\n\n"
            "MKV is the preferred format for high-quality video archiving and media center applications."
        ),
        "use_cases": [
            "Archive videos with multiple audio or subtitle tracks",
            "Prepare content for media center applications like Plex",
            "Convert for personal video library management",
        ],
        "related_tools": ["mp4_to_mov", "mp4_to_webm", "mp4_to_avi", "any_to_mp4"],
    },
    "mp4_to_flv": {
        "seo_title": "MP4 to FLV — Convert to Flash Video Format | FileForge",
        "seo_description": "Convert MP4 to Flash Video (FLV) format for legacy compatibility.",
        "long_description": (
            "Convert MP4 to FLV (Flash Video) — a legacy format that was once the standard for web video. "
            "While Flash is deprecated, FLV files are still needed for some legacy systems and archives.\n\n"
            "Useful for maintaining compatibility with older content management systems."
        ),
        "use_cases": [
            "Legacy system compatibility",
            "Archive conversion for old web content",
            "Specific CMS or platform requirements",
        ],
        "related_tools": ["mp4_to_webm", "mp4_to_mov", "any_to_mp4"],
    },
    "any_to_mp4": {
        "seo_title": "Video to MP4 — Convert Any Video to Universal MP4 | FileForge",
        "seo_description": "Convert MOV, AVI, WMV, MKV, FLV, WebM and other video formats to MP4. Universal compatibility.",
        "long_description": (
            "Convert virtually any video format — MOV, AVI, WMV, MKV, FLV, WebM, and more — "
            "to the universally compatible MP4 format. MP4 is supported by every modern device, browser, and platform.\n\n"
            "Uses H.264 video and AAC audio encoding for the best balance of quality and compatibility."
        ),
        "use_cases": [
            "Convert old video files to a modern, universal format",
            "Prepare videos for social media uploads",
            "Fix playback issues by converting to MP4",
            "Standardize a video library to one format",
        ],
        "related_tools": ["mp4_to_mov", "mp4_to_webm", "mp4_to_mkv", "mp4_to_mp3"],
    },

    # ── Excel / CSV Tools ─────────────────────────────────────────────────
    "csv_to_xlsx": {
        "seo_title": "CSV to Excel — Convert CSV to XLSX Spreadsheet | FileForge",
        "seo_description": "Convert CSV files to Excel XLSX spreadsheets. Auto-detects columns and formatting.",
        "long_description": (
            "Transform your CSV (comma-separated values) files into proper Excel XLSX spreadsheets. "
            "Columns are auto-detected and data types are preserved for immediate use in Excel.\n\n"
            "Ideal for converting exported data from databases, APIs, or other tools into a richer spreadsheet format."
        ),
        "use_cases": [
            "Import CSV data exports into Excel",
            "Convert database exports to spreadsheet format",
            "Prepare CSV files for non-technical colleagues who prefer Excel",
        ],
        "related_tools": ["xlsx_to_csv", "csv_to_html", "xlsx_to_pdf", "xlsx_to_html"],
    },
    "csv_to_html": {
        "seo_title": "CSV to HTML — Convert CSV Data to HTML Table | FileForge",
        "seo_description": "Convert CSV files to styled HTML tables. Ready to embed in websites or share.",
        "long_description": (
            "Convert your CSV data into a clean, styled HTML table with proper headers, borders, "
            "and alternating row colors. The output is a complete HTML document ready to open in any browser.\n\n"
            "Perfect for sharing data in a visually appealing format without requiring spreadsheet software."
        ),
        "use_cases": [
            "Create web-friendly data tables from CSV exports",
            "Share data with people who don't have Excel",
            "Embed data tables in websites or documentation",
        ],
        "related_tools": ["csv_to_xlsx", "xlsx_to_html", "xlsx_to_csv"],
    },
    "xlsx_to_csv": {
        "seo_title": "Excel to CSV — Convert XLSX to CSV | FileForge",
        "seo_description": "Convert Excel XLSX spreadsheets to CSV format. Simple, universal data export.",
        "long_description": (
            "Convert Excel spreadsheets to CSV — the universal data exchange format. CSV files "
            "can be imported into any database, programming language, or data analysis tool.\n\n"
            "The first sheet is exported with all data preserved in plain-text comma-separated format."
        ),
        "use_cases": [
            "Export Excel data for database import",
            "Convert spreadsheets for use in data science tools",
            "Create cross-platform compatible data files",
        ],
        "related_tools": ["csv_to_xlsx", "xlsx_to_html", "xlsx_to_pdf"],
    },
    "xlsx_to_html": {
        "seo_title": "Excel to HTML — Convert XLSX to HTML Table | FileForge",
        "seo_description": "Convert Excel spreadsheets to HTML tables for web display and sharing.",
        "long_description": (
            "Convert your Excel spreadsheet into a clean HTML table with proper headers and styling. "
            "The output is a standalone HTML page you can open in any browser or embed in a website.\n\n"
            "Great for sharing spreadsheet data with people who don't have Excel installed."
        ),
        "use_cases": [
            "Publish spreadsheet data on a website",
            "Share tabular data via email as HTML",
            "Convert Excel reports to web-viewable format",
        ],
        "related_tools": ["xlsx_to_csv", "csv_to_html", "xlsx_to_pdf", "csv_to_xlsx"],
    },
    "xlsx_to_pdf": {
        "seo_title": "Excel to PDF — Convert XLSX Spreadsheet to PDF | FileForge",
        "seo_description": "Convert Excel XLSX spreadsheets to professional PDF documents with formatted tables.",
        "long_description": (
            "Convert your Excel spreadsheets into polished PDF documents. Tables are rendered with "
            "professional styling, alternating row colors, and proper headers.\n\n"
            "Ideal for sharing finalized reports, financial statements, or data tables in a non-editable format."
        ),
        "use_cases": [
            "Share financial reports as PDF",
            "Create print-ready versions of spreadsheets",
            "Archive spreadsheet data in a fixed format",
        ],
        "related_tools": ["xlsx_to_csv", "xlsx_to_html", "csv_to_xlsx", "pdf_to_xlsx"],
    },

    # ── Text / PPTX Tools ────────────────────────────────────────────────
    "txt_to_pdf": {
        "seo_title": "TXT to PDF — Convert Plain Text to PDF | FileForge",
        "seo_description": "Convert plain text files to formatted PDF documents with monospace font and proper pagination.",
        "long_description": (
            "Transform plain text files into properly formatted PDF documents. Text is rendered in a clean "
            "monospace font with proper page breaks and margins — ideal for code, logs, or plain-text documents.\n\n"
            "The output PDF is print-ready with A4 page size and comfortable margins."
        ),
        "use_cases": [
            "Create printable PDFs from code or log files",
            "Format plain-text documents for professional sharing",
            "Archive text content in a universal format",
        ],
        "related_tools": ["txt_to_json", "pdf_to_txt", "docx_to_pdf"],
    },
    "txt_to_json": {
        "seo_title": "TXT to JSON — Convert Text to JSON Format | FileForge",
        "seo_description": "Wrap plain text content in a structured JSON object with line count and content fields.",
        "long_description": (
            "Convert a plain-text file into a structured JSON object containing the full text, "
            "individual lines as an array, and a line count. Perfect for feeding text data into APIs or applications.\n\n"
            "The output JSON is formatted with proper indentation for easy reading and parsing."
        ),
        "use_cases": [
            "Prepare text data for API consumption",
            "Convert configuration files to JSON format",
            "Feed text content into web applications",
        ],
        "related_tools": ["txt_to_pdf", "pdf_to_txt", "csv_to_xlsx"],
    },
    "pptx_to_pdf": {
        "seo_title": "PPTX to PDF — Convert PowerPoint to PDF | FileForge",
        "seo_description": "Convert PowerPoint PPTX presentations to PDF format. Each slide is preserved with text and layout.",
        "long_description": (
            "Convert your PowerPoint presentations to PDF format. Each slide's text content is extracted "
            "and rendered in a clean, readable PDF layout with proper slide numbering.\n\n"
            "Perfect for sharing presentations with people who don't have PowerPoint, "
            "or creating print-ready handouts from your slides."
        ),
        "use_cases": [
            "Share presentations as universally readable PDFs",
            "Create printable handouts from slide decks",
            "Archive presentations in a stable, long-term format",
        ],
        "related_tools": ["pdf_to_pptx", "docx_to_pptx", "docx_to_pdf", "txt_to_pdf"],
    },
}


def get_seo_data(url_name):
    """Return SEO dict for a given URL name, or sensible defaults."""
    return TOOL_SEO.get(url_name, {})


def get_related_tools(url_name, all_tools_flat):
    """
    Return a list of tool dicts for tools related to `url_name`.
    `all_tools_flat` should be a list of (name, desc, url_name, icon) tuples.
    """
    seo = TOOL_SEO.get(url_name, {})
    related_names = seo.get("related_tools", [])
    if not related_names:
        return []

    from django.urls import reverse
    tools = []
    for rname in related_names[:6]:  # max 6 related
        for name, desc, uname, icon in all_tools_flat:
            if uname == rname:
                tools.append({
                    "name": name,
                    "description": desc,
                    "url": reverse(uname),
                    "icon": icon,
                })
                break
    return tools
