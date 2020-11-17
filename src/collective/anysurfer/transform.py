# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from collective.anysurfer import _
from plone import api
from plone.transformchain.interfaces import ITransform
from zope.component import adapts
from zope.component.hooks import getSite
from zope.i18n import translate
from zope.interface import Interface, implementer


def remove_empty_lists(soup):
    """
    <ul class="navTree navTreeLevel1"></ul>
    """
    empty_tags = soup.findAll(
        lambda tag: tag.name == "ul"
        and not tag.contents
        and (tag.string is None or not tag.string.strip())
    )
    [empty_tag.extract() for empty_tag in empty_tags]


def fill_required_titles(soup):
    """
      <span class="required" title="Required">\xa0</span>
    -->
      <span class="required" title="Required"> (Required)</span>
    """
    current_lang = api.portal.get_current_language()[:2]
    translated_required = translate(_(u"Required"), target_language=current_lang)
    required_tags = soup.findAll(
        lambda tag: tag.name == "span"
        and tag.has_attr("title")
        and tag["title"] == translated_required
        and tag.has_attr("class")
        and "required" in tag["class"]
    )
    for tag in required_tags:
        tag.string = " ({0})".format(translated_required)


def assemble_required_labels(soup):
    """
      <label for="message">Message</label>
      <span class="fieldRequired" title="Required">(Required)</span>
    -->
      <label for="message">Message
        <span class="fieldRequired" title="Required">(Required)</span>
      </label>
    """
    labels = soup.findAll(lambda tag: tag.name == "label" and tag.has_attr("for"))
    for label in labels:
        next_tag = label.find_next_sibling(["label", "span"])
        if not next_tag or next_tag.name != "span":
            continue
        if next_tag.has_attr("class") and "fieldRequired" in next_tag["class"]:
            label.append(next_tag)


def replace_tags(soup):
    """
      <div replacetag="h2">
    -->
      <h2>
    """
    tags = soup.findAll(lambda tag: tag.has_attr("replacetag"))
    for tag in tags:
        replacing_tag = tag["replacetag"]
        tag.name = replacing_tag
        del tag["replacetag"]


def change_news_images_alt(soup):
    """
    We may not have the news title as alt
    """
    image_tags = soup.findAll(
        lambda tag: tag.name == "img"
        and tag.has_attr("class")
        and "newsImage" in tag["class"]
    )
    if not image_tags:
        return
    current_lang = api.portal.get_current_language()[:2]
    translated_news_alt = translate(
        _(u"News image - click to view full image"), target_language=current_lang,
    )
    for tag in image_tags:
        tag["alt"] = translated_news_alt


def add_alt_on_all_images(soup):
    """
    We need to have at alt on every images
    """
    image_tags = soup.findAll(lambda tag: tag.name == "img" and not tag.has_attr("alt"))
    for tag in image_tags:
        tag["alt"] = ""


@implementer(ITransform)
class AnySurfer(object):
    adapts(Interface, Interface)
    order = 9000

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def applyTransform(self):
        site = getSite()
        if not site:
            return False
        responseType = self.request.response.getHeader("content-type") or ""
        if not responseType.startswith("text/html") and not responseType.startswith(
            "text/xhtml"
        ):
            return False
        return True

    def transformBytes(self, result, encoding):
        if not self.applyTransform():
            return result
        soup = BeautifulSoup(result, "lxml")
        remove_empty_lists(soup)
        fill_required_titles(soup)
        assemble_required_labels(soup)
        replace_tags(soup)
        change_news_images_alt(soup)
        add_alt_on_all_images(soup)
        return str(soup)

    def transformUnicode(self, result, encoding):
        if not self.applyTransform():
            return result
        soup = BeautifulSoup(result, "lxml")
        remove_empty_lists(soup)
        fill_required_titles(soup)
        assemble_required_labels(soup)
        replace_tags(soup)
        change_news_images_alt(soup)
        add_alt_on_all_images(soup)
        return str(soup)

    def transformIterable(self, result, encoding):
        if not self.applyTransform():
            return result
        transformed = []
        for r in result:
            soup = BeautifulSoup(r, "lxml")
            remove_empty_lists(soup)
            fill_required_titles(soup)
            assemble_required_labels(soup)
            replace_tags(soup)
            change_news_images_alt(soup)
            add_alt_on_all_images(soup)
            transformed.append(str(soup))
        return transformed
