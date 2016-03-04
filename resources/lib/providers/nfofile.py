import sys
import xbmcvfs
from abc import ABCMeta
from contextlib import closing
import xml.etree.ElementTree as ET

if sys.version_info < (2, 7):
    from xml.parsers.expat import ExpatError as ParseError
else:
    from xml.etree.ElementTree import ParseError

import mediatypes
from sorteddisplaytuple import SortedDisplay

class NFOFileAbstractProvider(object):
    __metaclass__ = ABCMeta
    name = SortedDisplay('file:nfo', 'NFO file')

    def build_resultimage(self, url, title):
        resultimage = {'url': url, 'provider': self.name, 'preview': url}
        resultimage['title'] = '<{0}>'.format(title)
        resultimage['rating'] = SortedDisplay(0, '')
        resultimage['size'] = SortedDisplay(0, '')
        resultimage['language'] = 'xx'
        return resultimage

class NFOFileSeriesProvider(NFOFileAbstractProvider):
    mediatype = mediatypes.TVSHOW

    def get_exact_images(self, path):
        path += 'tvshow.nfo'
        result = {}

        root = read_nfofile(path)
        if root is None or root.find('art') is None:
            return {}
        artlistelement = root.find('art')
        if artlistelement is None:
            return {}
        for artelement in artlistelement:
            if artelement.tag == 'season':
                num = int(artelement.attrib['num'])
                for seasonartelement in artelement:
                    arttype = 'season.{0}.{1}'.format(num, seasonartelement.tag)
                    result[arttype] = self.build_resultimage(seasonartelement.text, arttype)
            else:
                result[artelement.tag] = self.build_resultimage(artelement.text, artelement.tag)
        return result

class NFOFileMovieProvider(NFOFileAbstractProvider):
    mediatype = mediatypes.MOVIE

    def get_exact_images(self, path):
        longnfopath = path.rsplit('.', 1)[0] + '.nfo'
        if path.count('/'):
            nfopath = path.rsplit('/', 1)[0] + '/movie.nfo'
        else:
            nfopath = path.rsplit('\\', 1)[0] + '/movie.nfo'
        result = {}

        root = read_nfofile(longnfopath)
        if root is None or root.find('art') is None:
            root = read_nfofile(nfopath)
            if root is None or root.find('art') is None:
                return {}
        artlistelement = root.find('art')
        if artlistelement is not None:
            for artelement in artlistelement:
                result[artelement.tag] = self.build_resultimage(artelement.text, artelement.tag)
        return result

class NFOFileEpisodeProvider(NFOFileAbstractProvider):
    mediatype = mediatypes.EPISODE

    def get_exact_images(self, path):
        path = path.rsplit('.', 1)[0] + '.nfo'
        result = {}

        root = read_nfofile(path)
        if root is None or root.find('art') is None:
            return {}
        artlistelement = root.find('art')
        for artelement in artlistelement:
            result[artelement.tag] = self.build_resultimage(artelement.text, artelement.tag)
        return result

def read_nfofile(filename):
    if not xbmcvfs.exists(filename):
        return None
    with closing(xbmcvfs.File(filename)) as nfofile:
        try:
            return ET.parse(nfofile).getroot()
        except ParseError:
            pass
        # maybe it's all XML except the last line, like the wiki suggests for XML + URL
        nfofile.seek(0, 0)
        lines = nfofile.read().split('\n')
        while lines and not lines[-1]:
            del lines[-1]
        if lines:
            del lines[-1]
        if lines:
            try:
                return ET.XML('\n'.join(lines))
            except ParseError:
                pass