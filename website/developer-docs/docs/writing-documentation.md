---
title: Writing documentation
---

Writing documentation for authentik is a great way for both new and experienced users to improve and contribute to the project. Here are a few guidelines to ensure
the documentation is easy to read and uses similar phrasing.

# General guidelines

- authentik should always be stylized as `authentik` (with a lower-case a and ending with a k)
- Documentation should use American english
- Feel free to use Docusaurus-specific features, see [here](https://docusaurus.io/docs/next/markdown-features)
- Use abbreviations where it makes sense (for commonly used terms like SAML and OAuth)
- Phrasing should never blame the user, and should be subjective, i.e

    - **DON'T** `You may never click x.`
    - **DO** `x should never be clicked.`

- When referring to other objects in authentik, use cursive text, and link to the corresponding documentation if possible.
- When referring to external tools, give an example how to use the tools or explain how the user can use them.
- Make sure to add the documentation to add to the sidebar, if adding a new page.
- Test how the documentation renders using the Netlify Preview, especially when using Docusaurus-specific features.

If you find any documentation that doesn't match these guidelines, feel free to either open an Issue or a PR so they can be fixed.

## Integration guidelines

These guidelines apply in addition to the ones above.

- For placeholders, use angle brackets (`<placeholder-name>`).

    Make sure to also define if the placeholder is something the user needs to define, something another system defines, or randomly generated.

    If you're adding configuration snippets to the documentation, and the snippet is in a language that supports comments,
    other placeholders may be used, for example comments referencing an earlier step.

- For placeholder domains, use `authentik.company` and `app-name.company`, where `app-name` is the name of the application you are writing documentation for.
- Try to order the documentation in the order that makes it easiest for the user to configure.
