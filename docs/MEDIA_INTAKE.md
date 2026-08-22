# Real media intake

The website should prefer real Kodo artifacts over decorative AI imagery.

## Admission gate

A media asset may be marked `real` only if all are true:

- it is actual Kodo project output;
- public display is acceptable to the team;
- it contains no private Discord/user data, credentials, local paths, or sensitive debug information;
- the caption does not imply a metric or result that was not measured;
- third-party game imagery is presented as project target/context and does not imply affiliation with Supercell.

## Hero replacement

Place the file at, for example:

`assets/kodo-environment.webp`

Then edit `media-manifest.js`:

```js
hero: {
  mode: "real",
  src: "./assets/kodo-environment.webp",
  alt: "Kodo environment showing ...",
  caption: "Kodo environment build, captured ..."
}
```

If `mode` remains `conceptual`, the website keeps the schematic fallback.
