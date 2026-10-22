export const meta = {
  name: 'amie-seo-geo-categories',
  description: 'SEO/GEO pipeline: writer agents draft category copy, reviewer agents check brand, claims and SEO rules; output is drafts for approval (no store writes)',
  whenToUse: 'Drafting SEO + GEO copy for a\'mie store categories or pages before human approval',
  phases: [
    { title: 'Write', detail: 'one writer per pair of categories' },
    { title: 'Review', detail: 'one reviewer per pair: brand voice, claims, SEO limits, links' },
  ],
}

const RULES = `
Brand: a'mie (ايمي)، براند سعودي للعناية بالجسم، amie-sa.com على منصة زد. الشعار: rooted in nature, defined by luxury.
صوت البراند: دافئ وقريب، راقٍ بدون تكلّف، واثق بدون مبالغة، لغة عربية فصحى بسيطة يفهمها الجميع، تخاطب المرأة بصيغة المؤنث ("اختاري"، "بشرتك"). بدون إيموجي.
الجمهور: نساء 24–45 في السعودية والخليج.
ممنوعات صارمة:
- أي ادعاء غير موثق: لا "علاج" ولا "يعالج"، لا "آمن للحامل/للأطفال"، لا "طاقة سلبية"، لا نتائج طبية أو نسب مئوية أو "مثبت علمياً"، لا "طبيعي 100%".
- لا ذكر للدفع عند الاستلام.
- لا ذكر لأي براند منافس ولا لمصادر أرقام البحث.
- لا أسعار.
- استخدمي فقط الحقائق المعطاة عن المنتجات (المكونات، الأحجام، الروائح). لا تخترعي مكونات أو مزايا.
- الروابط الداخلية: فقط من قائمة الروابط المعطاة، بصيغة HTML <a href="URL">نص</a>.
`

const LINKS = args.links

const OUT = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          name: { type: 'string' },
          description_html: { type: 'string', description: 'HTML: 2-3 <p> paragraphs, 80-150 Arabic words, includes 2 internal <a> links' },
          seo_title: { type: 'string', description: '<=60 chars, ends with | ايمي a\'mie' },
          meta_description: { type: 'string', description: '<=155 chars' },
          faqs: { type: 'array', items: { type: 'object', properties: { q: { type: 'string' }, a: { type: 'string' } }, required: ['q', 'a'] } },
          keywords_used: { type: 'array', items: { type: 'string' } },
          review_notes: { type: 'string' },
        },
        required: ['id', 'name', 'description_html', 'seo_title', 'meta_description', 'faqs', 'keywords_used'],
      },
    },
  },
  required: ['items'],
}

const fmt = c => `- القسم: ${c.name} (id ${c.id})، رابطه: ${c.url}
  الكلمات المستهدفة (بحث شهري في السعودية): ${c.keywords}
  المنتجات والحقائق: ${c.facts}
  لينكات داخلية مقترحة لأقسام مرتبطة: ${c.linkTo.join('، ')}`

const results = await pipeline(
  args.pairs,
  (pair, _o, i) => agent(`أنت كاتب SEO وGEO (الظهور في إجابات محركات الذكاء الاصطناعي) لمتجر a'mie. اكتب محتوى قسمين من أقسام المتجر.
${RULES}
روابط الأقسام المسموح بها:
${LINKS}

لكل قسم اكتب:
1. description_html: وصف 80–150 كلمة في 2–3 فقرات <p>. أول جملة تقول بوضوح القسم فيه إيه وتحتوي الكلمة الأساسية (الأعلى بحثاً المناسبة). اذكر أسماء منتجات وحقائق محددة. أدرج لينكين داخليين طبيعيين لأقسام مرتبطة من القائمة. أسلوب البراند.
2. seo_title: حد أقصى 60 حرفاً، يبدأ بالكلمة الأساسية، وينتهي بـ "| ايمي a'mie".
3. meta_description: حد أقصى 155 حرفاً، فيه الكلمة الأساسية ودعوة ناعمة للتسوق.
4. faqs: 3 أسئلة يسألها الناس فعلاً عن هذا النوع من المنتجات، بإجابات مباشرة 1–2 جملة قابلة للاقتباس، من الحقائق المعطاة فقط.
5. keywords_used: الكلمات المستهدفة التي استخدمتها فعلاً.

القسمان:
${pair.map(fmt).join('\n')}`, { label: `write:${pair.map(c => c.name).join('+')}`, phase: 'Write', schema: OUT }),
  (draft, pair) => agent(`أنت مراجع صارم لمحتوى SEO/GEO لبراند a'mie. راجع المسودة التالية وصحّحها، ثم أرجع النسخة النهائية بنفس البنية.
${RULES}
روابط الأقسام المسموح بها:
${LINKS}

الحقائق الصحيحة للمنتجات (أي معلومة خارجها تُحذف):
${pair.map(fmt).join('\n')}

افحص وصحّح:
- أي ادعاء ممنوع أو مبالغ فيه أو معلومة غير موجودة في الحقائق ← احذفه أو أعد صياغته.
- طول seo_title ≤ 60 حرفاً (عدّ الحروف فعلياً) و meta_description ≤ 155 حرفاً ← اختصر إن لزم.
- الوصف 80–150 كلمة، أول جملة فيها الكلمة الأساسية، ولينكان داخليان صحيحان من القائمة فقط وبصيغة HTML سليمة.
- صوت البراند: دافئ، راقٍ، بسيط، بصيغة المؤنث، بدون إيموجي.
- الأسئلة الشائعة واقعية وإجاباتها مباشرة ومن الحقائق.
في review_notes اكتب باختصار ما غيّرته ولماذا (أو "لا تغييرات").

المسودة:
${JSON.stringify(draft)}`, { label: `review:${pair.map(c => c.name).join('+')}`, phase: 'Review', schema: OUT }),
)

return results.filter(Boolean).flatMap(r => r.items)
