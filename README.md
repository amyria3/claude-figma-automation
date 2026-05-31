{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Claude + Figma Automation\
\
Complete reference and workflows for automating Figma with Claude via MCP.\
\
## 
\f1 \uc0\u55357 \u56538 
\f0  Documentation\
\
### 1. **FIGMA_WORKFLOW_TECHNISCH.md**\
- Pre-flight checklist (vor jeder Task)\
- Font-loading patterns\
- Verification methods (get_metadata)\
- Error handling\
- Golden rules & best practices\
\
### 2. **FIGMA_API_REFERENCE_FINAL.md**\
- Complete API reference with code examples\
- Text operations (changing, fonts, typography)\
- Styling operations (colors, fills, strokes)\
- Flex layouts (VERTICAL, HORIZONTAL, alignment)\
- Known limitations & workarounds\
- Quick-start templates\
\
### 3. **FIGMA_STYLESHEET_WORKAROUND.md**\
- Stylesheet-based styling workflow (for Variables limitation)\
- Step-by-step guide\
- Design token templates (copy-paste ready)\
- Checklists for both Claude and user\
\
## 
\f1 \uc0\u55356 \u57263 
\f0  Quick Start\
\
1. Create design tokens/stylesheet in Figma\
2. Share screenshot with Claude\
3. Claude parses values and applies to elements\
4. User manually links to Figma Variables\
\
## 
\f1 \uc0\u9989 
\f0  Feature Status\
\
| Feature | Status | Notes |\
|---------|--------|-------|\
| Text operations | 
\f1 \uc0\u9989 
\f0  Working | All typography properties supported |\
| Styling (colors, fills) | 
\f1 \uc0\u9989 
\f0  Working | Can read & apply colors |\
| Flex layouts | 
\f1 \uc0\u9989 
\f0  Working | VERTICAL, HORIZONTAL, alignment |\
| Node operations | 
\f1 \uc0\u9989 
\f0  Working | Create, delete, rename |\
| Verification via get_metadata() | 
\f1 \uc0\u9989 
\f0  Working | XML-based confirmation |\
| Variables (create/link) | 
\f1 \uc0\u10060 
\f0  Not supported | Workaround available in doc #3 |\
\
## 
\f1 \uc0\u55357 \u56599 
\f0  How Claude Uses This\
\
- Store in GitHub\
- Claude accesses via GitHub Connector (when enabled)\
- Single source of truth for all Figma automation workflows\
- Consistent across all chats\
\
## 
\f1 \uc0\u55357 \u56541 
\f0  Last Updated\
\
May 31, 2026\
\
## 
\f1 \uc0\u55357 \u56481 
\f0  Related\
\
- [Figma Plugin API Docs](https://www.figma.com/plugin-docs/)\
- [Claude MCP Documentation](https://docs.anthropic.com/)}