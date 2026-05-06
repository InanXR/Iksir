## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[2] Iksir-Italic.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: h	Contours detected: 2	Expected: 1

- Glyph name: m	Contours detected: 2	Expected: 1

- Glyph name: n	Contours detected: 2	Expected: 1

- Glyph name: r	Contours detected: 2	Expected: 1

- Glyph name: u	Contours detected: 2	Expected: 1

- Glyph name: u0195	Contours detected: 2	Expected: 1

- 85 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* .notdef: B&lt;&lt;239.0,396.0&gt;-&lt;240.0,394.0&gt;-&lt;242.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: L&lt;&lt;345.0,170.0&gt;--&lt;345.0,171.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;241.0,215.0&gt;-&lt;241.0,212.0&gt;-&lt;242.0,211.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: L&lt;&lt;332.0,439.0&gt;--&lt;332.0,440.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;289.0,472.0&gt;-&lt;289.0,473.0&gt;-&lt;288.0,473.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;241.0,478.0&gt;-&lt;241.0,477.0&gt;-&lt;243.0,476.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;332.0,440.0&gt;-&lt;332.0,442.0&gt;-&lt;331.0,442.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;332.0,202.0&gt;-&lt;330.0,202.0&gt;-&lt;330.0,207.0&gt;&gt; has the same coordinates as a previous segment.

* uni09A709CD09AE.akhn: L&lt;&lt;679.0,9.0&gt;--&lt;692.0,71.0&gt;&gt; has the same coordinates as a previous segment.

* uni09B209CD09AE.akhn: L&lt;&lt;596.0,196.0&gt;--&lt;610.0,258.0&gt;&gt; has the same coordinates as a previous segment.

* uni09B609CD09AE.akhn: L&lt;&lt;659.0,195.0&gt;--&lt;672.0,257.0&gt;&gt; has the same coordinates as a previous segment.

* uni09DD09CD09F0.blwf: L&lt;&lt;319.0,63.0&gt;--&lt;316.0,49.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>
</div>
</details>

<details><summary>[2] Iksir-Regular.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: grave	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: h	Contours detected: 2	Expected: 1

- Glyph name: m	Contours detected: 2	Expected: 1

- Glyph name: n	Contours detected: 2	Expected: 1

- Glyph name: r	Contours detected: 2	Expected: 1

- Glyph name: u	Contours detected: 2	Expected: 1

- Glyph name: u0195	Contours detected: 2	Expected: 1

- 83 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* .notdef: B&lt;&lt;239.0,396.0&gt;-&lt;240.0,394.0&gt;-&lt;242.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: L&lt;&lt;345.0,170.0&gt;--&lt;345.0,171.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;241.0,215.0&gt;-&lt;241.0,212.0&gt;-&lt;242.0,211.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: L&lt;&lt;332.0,439.0&gt;--&lt;332.0,440.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;289.0,472.0&gt;-&lt;289.0,473.0&gt;-&lt;288.0,473.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;241.0,478.0&gt;-&lt;241.0,477.0&gt;-&lt;243.0,476.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;332.0,440.0&gt;-&lt;332.0,442.0&gt;-&lt;331.0,442.0&gt;&gt; has the same coordinates as a previous segment.

* .notdef: B&lt;&lt;332.0,202.0&gt;-&lt;330.0,202.0&gt;-&lt;330.0,207.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 4 | 71 | 6 | 161 | 0 | 
| 0% | 0% | 0% | 2% | 29% | 2% | 67% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
