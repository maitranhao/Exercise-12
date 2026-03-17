def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        # Dịch chuyển start dựa trên chunk_size trừ đi overlap 
        # để giữ ngữ cảnh giữa các đoạn
        start += (chunk_size - overlap) 
    return chunks