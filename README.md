
# Language/Region codes: a list of likely combinations

## Short summary

The main payload of this repository is the file **src/data/language_region_codes.txt**, which contains a researched set of *likely* language/region codes such as **en-us** or **ja-jp**.  It can be used to validate a field containing such language/region codes.

The file is in a simple format (tab-separated columns) which is deliberately agnostic in terms of programming language.

For the convenience of Python programmers, this package also includes some Python3 wrapper code which loads the file and has a convenience method for determining whether a language/region code is in the set of likely code combinations.  However, the file was deliberately not expressed as a data structure embedded in Python code; you can read and parse the file from whatever programming language you prefer.

## Rationale

* Two-character language codes are defined in ISO 639-1.
* Two-character region (country) codes are defined in ISO 3166-1 alpha-2.

However, the ISO standards do not define a set of valid **combinations** of language code and region code.  As far as the ISO standards are concerned, **mn-ie** (Mongolian as written in Ireland) and **cs-jm** (Czech as written in Jamaica) are just as valid as **en-us** (English as written in the United States) or **ja-jp** (Japanese as written in Japan).

One approach to validating a language/region field is to validate the language code and the region code separately, by confirming that each is officially defined in its corresponding standard (**en** is a valid language code, and **us** is a valid country/region code).  However, this approach will miss some cases which are almost certainly mistakes.

For example, in one collection of online linguistic data, I observed some Arabic data labeled with the combination **ar-ar**, which (according to the ISO codes) means "Arabic as written in Argentina".  This is almost certainly not what the creator of the data intended; the creator may have meant "Arabic as written in (Saudi) Arabia" (which would correctly be denoted **ar-sa**), or perhaps wasn't sure what region code to use and just followed the pattern found in some frequently observed combinations where the language code and region code happen to be the same (**de-de**, **es-es**, **fr-fr**, **it-it**).

The need to validate language/region is a common enough use case that I was surprised that I could not find any existing list of likely combinations of language and region codes.  So, I researched and prepared a list.


## Design considerations

There can obviously be no definitive list of likely combinations of language and region codes, because there is no fully objective criterion for judging a combination to be "likely".  If you need to indicate that some data is in Mongolian as written in Ireland, **mn-ie** is the correct way to label it.  It is correct but unlikely.

The rule of thumb followed here is that a combination is judged to be "likely" if it has been observed, or could plausibly be observed, as a supported language/region combination in a software product by a major international software vendor (Microsoft, Google, etc.), or in a major repository of modern (i.e. not historical) language data prepared for use in Natural Language Processing.  Some languages, such as Somali, Pashto, or Uighur, might be considered of lower interest from the perspective of international business, but are of interest from a military/intelligence standpoint; languages in this category tend to be found in some collections of linguistic data and therefore are included.

The list represents an informed set of judgment calls; the author holds a Ph.D. in Linguistics are has been working in Natural Language Processing in various capacities since the 1990s.  However, it must be emphasized that there is some irreducible subjectivity in judging what should be included.  Reports of factually mistaken information are, of course, welcome.


## How the list was prepared

* I searched the web for lists of languages or language/region combinations supported by various major vendors:

  * Microsoft (various products)
  * Google Translate
  * Lingoes
  * OPUS (an open-source repository of machine translation data)
  * etc.

* I programatically compared the language codes against ISO 639-1, and the region codes against ISO 3166-1 alpha-2. I flagged any non-compliant codes and resolved them by hand (either correcting the error, or simply discarding the item if the correct version was already in the list from another source).

* I manually checked over the language-region combinations to make sure each one looks reasonable, meaning that the indicated language is spoken by a significant population in the indicated country. This is where I weeded out cases such as **ar-ar** (Arabic/Argentina). In cases where I was uncertain or didn’t know where a language is spoken, I consulted standard references to verify that the combination was a reasonable one. For example, Wikipedia confirms that Divehi is primarily spoken in Maldives.

* Sometimes, a vendor listed only a language code (e.g. **sd** = Sindhi) with no country code. In the case of a language where none of the vendors included a country code, I added one by researching the most likely country or countries. In the case of Sindhi, for example, I added **sd-in** (India) and **sd-pk** (Pakistan).

* I excluded any language which has no two-letter code. For example, Google Translate supports Hawaiian, which has a three-letter code (**haw**), but has no two-letter code.  This was a very unusual case, because the languages supported by major international vendors nearly always have two-letter codes.  A list containing three-letter codes would be a separate project; the present project is to provide a means for validating fields of the form **en-us**.

There are some ISO 639-1 codes which don't appear in the list below. For example, ISO 639-1 has codes for Latin, Esperanto, Manx, Fulah, and Nauru. I didn't include these languages in the list, for the simple reason that they didn't appear in any of the vendor sources that I consulted listing languages supported in actual software products. The point is not to cover every language, but rather to cover languages likely to be encountered in the context of commercial software.

The ISO codes are up-to-date as of May 2018. Be aware that the ISO does occasionally make revisions to the country codes, reflecting changing political situations.

To the best of my knowledge, the information in the list is accurate as of May 2018. However, I make no guarantees regarding the list. I also don’t guarantee that I will keep the list continuously updated to reflect changes in the ISO standards. Reports of mistakes are of course welcome. 

## Intellectual property considerations

Under U.S. copyright law, facts cannot be copyrighted. A collection of facts can sometimes be copyrighted if the author exercised substantial creativity in the selection or arrangement of facts. In the unlikely event that I created any copyrightable interest in the list, I hereby assign the list to the public domain.

Also, I formally confirmed that my former employer (at the time I prepared the list) is making no intellectual property claim regarding the list under the terms of my employment contract. So, you can use the list as you please.

As for the Python code, I assign it to the public domain.  You may use it as you please.


