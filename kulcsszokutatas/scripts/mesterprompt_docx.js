const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, LevelFormat, AlignmentType, BorderStyle, PageBreak,
  Footer, PageNumber } = require('docx');

const content = require(path.resolve(__dirname, 'mesterprompt_content.js'));
const [outDocx, outMd] = process.argv.slice(2);
const GREEN = '2E7D32';
const TABLE_W = 9026; // A4, 2,54 cm margók

let numRef = 0;
const numberingConfigs = [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•',
  alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }];
const children = [];
const md = [];

for (const blk of content) {
  if (blk.title) {
    children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(blk.title)] }));
    md.push(`# ${blk.title}\n`);
  } else if (blk.h1) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(blk.h1)] }));
    md.push(`## ${blk.h1}\n`);
  } else if (blk.h2) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(blk.h2)] }));
    md.push(`### ${blk.h2}\n`);
  } else if (blk.h3) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun(blk.h3)] }));
    md.push(`#### ${blk.h3}\n`);
  } else if (blk.p) {
    children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun(blk.p)] }));
    md.push(`${blk.p}\n`);
  } else if (blk.q) {
    children.push(new Paragraph({
      spacing: { before: 80, after: 120 }, indent: { left: 360 },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: GREEN, space: 8 } },
      shading: { type: ShadingType.CLEAR, color: 'auto', fill: 'F1F8F1' },
      children: [new TextRun({ text: blk.q, italics: true })] }));
    md.push(`> ${blk.q}\n`);
  } else if (blk.b) {
    for (const t of blk.b) children.push(new Paragraph({ numbering: { reference: 'bullets', level: 0 }, spacing: { after: 60 }, children: [new TextRun(t)] }));
    md.push(blk.b.map(t => `- ${t}`).join('\n') + '\n');
  } else if (blk.n) {
    const ref = `num${numRef++}`;
    numberingConfigs.push({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.',
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } } } }] });
    for (const t of blk.n) children.push(new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { after: 80 }, children: [new TextRun(t)] }));
    md.push(blk.n.map((t, i) => `${i + 1}. ${t}`).join('\n') + '\n');
  } else if (blk.t) {
    const { widths, rows } = blk.t;
    const border = { style: BorderStyle.SINGLE, size: 4, color: 'BDBDBD' };
    const borders = { top: border, bottom: border, left: border, right: border };
    children.push(new Table({
      width: { size: TABLE_W, type: WidthType.DXA }, columnWidths: widths,
      rows: rows.map((r, ri) => new TableRow({ tableHeader: ri === 0, children: r.map((c, ci) => new TableCell({
        borders, width: { size: widths[ci], type: WidthType.DXA },
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: GREEN } : undefined,
        children: [new Paragraph({ children: [new TextRun({ text: c, bold: ri === 0, color: ri === 0 ? 'FFFFFF' : undefined })] })] })) })) }));
    children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    md.push(`| ${rows[0].join(' | ')} |\n|${rows[0].map(() => '---').join('|')}|\n` + rows.slice(1).map(r => `| ${r.join(' | ')} |`).join('\n') + '\n');
  } else if (blk.pagebreak) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
    md.push('---\n');
  }
}

const doc = new Document({
  creator: 'Claude Code', title: 'Kategóriafa- és kulcsszókutató ügynök – Mesterprompt',
  styles: {
    default: { document: { run: { font: 'Calibri', size: 22 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { size: 40, bold: true, color: GREEN }, paragraph: { spacing: { after: 200 } } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true, color: GREEN }, paragraph: { spacing: { before: 360, after: 160 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: '1B5E20' }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 23, bold: true, color: '33691E' }, paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: numberingConfigs },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: ['Mesterprompt – ', PageNumber.CURRENT, '. oldal'], size: 18, color: '757575' })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(outDocx, buf); fs.writeFileSync(outMd, md.join('\n')); console.log('OK'); });
