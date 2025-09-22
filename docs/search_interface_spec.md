
# Technical Knowledge Search Interface

## Search Capabilities

1. **Full-text search** across all technical messages
2. **Category filtering** (GitHub API, Social Media, Python, etc.)
3. **Content type filtering** (code blocks, URLs, API endpoints)
4. **Conversation-based grouping** of results
5. **Relevance scoring** based on keyword matches

## Search Syntax

- Basic search: `github api`
- Category filter: `category:github_api`
- Has code: `has:code` 
- Has URLs: `has:urls`
- Author filter: `author:user` or `author:assistant`
- Date range: `after:2024-01-01`

## API Endpoints

- `GET /search?q={query}&category={cat}&limit={n}`
- `GET /categories` - List all available categories
- `GET /stats` - Knowledge base statistics
- `GET /entry/{id}` - Get full content of specific entry

## Example Queries

- `github api authentication` - Find GitHub auth examples
- `category:social_media_api instagram` - Instagram API content
- `python automation has:code` - Python scripts with code
- `error fix deployment` - Deployment troubleshooting
