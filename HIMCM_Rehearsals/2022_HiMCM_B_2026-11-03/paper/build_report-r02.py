#!/usr/bin/env python3
"""Render an evidence-bound manuscript. No data fitting or result calculation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

FONT_ROOT = Path('/Users/ericzhang/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name, filename in [('Body','DejaVuSans.ttf'),('Body-Bold','DejaVuSans-Bold.ttf'),('Body-Italic','DejaVuSans-Oblique.ttf'),('Body-BoldItalic','DejaVuSans-BoldOblique.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONT_ROOT/filename)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Italic',boldItalic='Body-BoldItalic')

INK = colors.HexColor('#18383E')
TEAL = colors.HexColor('#176A73')
MUTED = colors.HexColor('#586B70')
LINE = colors.HexColor('#D6E2E4')
PALE = colors.HexColor('#EDF5F5')
CAUTION = colors.HexColor('#FAF4E7')
WIDTH = 512
STYLES = {
 'body': ParagraphStyle('body',fontName='Body',fontSize=9.7,leading=14.1,textColor=INK,spaceAfter=8,allowWidows=0,allowOrphans=0),
 'reference': ParagraphStyle('reference',fontName='Body',fontSize=8.6,leading=12.3,textColor=INK,spaceAfter=8),
 'kicker': ParagraphStyle('kicker',fontName='Body-Bold',fontSize=8.3,leading=11,textColor=TEAL,spaceAfter=7),
 'title': ParagraphStyle('title',fontName='Body-Bold',fontSize=22,leading=27,textColor=INK,spaceAfter=13),
 'deck': ParagraphStyle('deck',fontName='Body',fontSize=13,leading=18,textColor=MUTED,spaceAfter=17),
 'h2': ParagraphStyle('h2',fontName='Body-Bold',fontSize=11,leading=15,textColor=TEAL,spaceBefore=6,spaceAfter=6,keepWithNext=True),
 'equation': ParagraphStyle('equation',fontName='Body',fontSize=10.1,leading=16,textColor=INK,spaceAfter=8,leftIndent=9),
 'table': ParagraphStyle('table',fontName='Body',fontSize=8.1,leading=11.6,textColor=INK),
 'tablehead': ParagraphStyle('tablehead',fontName='Body-Bold',fontSize=8,leading=11.2,textColor=colors.white),
 'callout': ParagraphStyle('callout',fontName='Body',fontSize=9,leading=13.1,textColor=INK),
 'callouthead': ParagraphStyle('callouthead',fontName='Body-Bold',fontSize=9.2,leading=13.1,textColor=INK,spaceAfter=4),
 'bullet': ParagraphStyle('bullet',fontName='Body',fontSize=9.5,leading=13.5,textColor=INK,leftIndent=12,firstLineIndent=-10,spaceAfter=4)
}

def para(text: str, style: str='body'):
    return Paragraph(text, STYLES[style])

def render_block(block):
    kind = block['type']
    if kind in ('p','h2','equation','reference'):
        return [para(block['text'],{'p':'body'}.get(kind,kind))]
    if kind == 'bullets':
        return [para('- ' + x,'bullet') for x in block['items']] + [Spacer(1,4)]
    if kind == 'callout':
        contents = [para(block['title'],'callouthead'),para(block['text'],'callout')]
        box = Table([[contents]],colWidths=[WIDTH],hAlign='LEFT')
        box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CAUTION),('BOX',(0,0),(-1,-1),0.5,colors.HexColor('#E1D5B7')),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
        return [box,Spacer(1,10)]
    if kind == 'table':
        rows = [[para(escape(x),'tablehead') for x in block['header']]]
        rows += [[para(escape(str(x)),'table') for x in row] for row in block['rows']]
        table = Table(rows,colWidths=[WIDTH*x for x in block['widths']],repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),0.5,INK),('LINEBELOW',(0,1),(-1,-1),0.3,LINE),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
        return [table,Spacer(1,11)]
    raise ValueError(f'Unknown block type: {kind}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    args = ap.parse_args()
    spec = json.loads(args.source.read_text())
    project = args.source.resolve().parent.parent
    manifest = project / spec['accepted_manifest']
    assert hashlib.sha256(manifest.read_bytes()).hexdigest()==spec['accepted_manifest_sha256'], 'Accepted manifest identity changed'
    if args.output.exists():
        raise FileExistsError('Preserve prior exports; choose a new revision path')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    doc = SimpleDocTemplate(str(args.output),pagesize=letter,rightMargin=50,leftMargin=50,topMargin=56,bottomMargin=47,title=spec['title'],author='Retrospective HiMCM practice',subject=spec['status'],pageCompression=1)
    story=[]
    page_titles=[]
    for i,page in enumerate(spec['pages']):
        if i:
            story.append(PageBreak())
        story.extend([para(page['kicker'],'kicker'),para(page['title'],'title')])
        if page.get('deck'):
            story.append(para(page['deck'],'deck'))
        for block in page['blocks']:
            story.extend(render_block(block))
        page_titles.append(page['title'])
    def furniture(canvas,doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.line(50,756,562,756)
        canvas.setFont('Body-Bold',7.3)
        canvas.setFillColor(TEAL)
        canvas.drawString(50,764,'2022 HiMCM B | RETROSPECTIVE PRACTICE')
        canvas.setFillColor(colors.HexColor('#925D19'))
        canvas.drawRightString(562,764,spec['status'])
        canvas.setStrokeColor(LINE)
        canvas.line(50,36,562,36)
        canvas.setFont('Body',7)
        canvas.setFillColor(MUTED)
        canvas.drawString(50,24,spec['revision']+' | Methods and export checkpoint')
        canvas.drawRightString(562,24,str(doc.page))
        canvas.restoreState()
    doc.build(story,onFirstPage=furniture,onLaterPages=furniture)
    from pypdf import PdfReader
    reader=PdfReader(args.output)
    if len(reader.pages)!=len(spec['pages']):
        raise RuntimeError(f'Unexpected page spill: planned {len(spec["pages"])}, actual {len(reader.pages)}')
    for page,title in zip(reader.pages,page_titles):
        text=page.extract_text()
        if ' '.join(title.split()) not in ' '.join(text.split()):
            raise RuntimeError(f'Planned title missing from page: {title}')
        if spec['status'] not in text:
            raise RuntimeError('Draft status missing')
    print(json.dumps({'source':str(args.source.resolve()),'source_sha256':hashlib.sha256(args.source.read_bytes()).hexdigest(),'output':str(args.output.resolve()),'output_sha256':hashlib.sha256(args.output.read_bytes()).hexdigest(),'pages':len(reader.pages),'draft_status_on_every_page':True},indent=2))

if __name__=='__main__':
    main()
