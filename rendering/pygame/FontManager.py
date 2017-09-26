#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Base class for Rendering on pygame.

http://pygame.org/wiki/SimpleFontManager

TODO:

"""

import pygame
from pygame import QUIT

class font_manager:
    '''
    A simple class used to manage Font objects and provide a simple way to use
    them to draw text on any surface.

    Directly import this file to use the class, or run this file from the
    command line to see a trivial sample.

    Written by Scott O. Nelson
    '''
    def __init__(self, listOfFontNamesAndSizesAsTuple):
        '''
        Pass in a tuple of 2-item tuples.  Each 2-item tuple is a fontname /
        size pair. To use the default font, pass in a None for the font name.
        Font objects are created for each of the pairs and can then be used
        to draw text with the Draw() method below.

        Ex: fontMgr = cFontManager(((None, 24), ('arial', 18), ('arial', 24),
            ('courier', 12), ('papyrus', 50)))

        TODO: add support for bold & italics
        '''
        self._fontDict = {}
        for pair in listOfFontNamesAndSizesAsTuple:
            assert len(pair) == 2, \
                "Pair must be composed of a font name and a size - ('arial', 24)"
            font_name = pair[0]
            font_name = None # TODO: Luis added this for the stupid thing to stop complaining.
            if font_name:
                fontFullFileName = pygame.font.match_font(font_name)
                assert fontFullFileName, 'Font: %s Size: %d is not available.' % pair
            else:
                fontFullFileName = None # use default font
            self._fontDict[pair] = pygame.font.Font(fontFullFileName, pair[1])

    def Draw(self, surface, font_name, size, text, rect_or_pos_to_draw_to, color,
             align_horiz='left', align_vert='top', anti_alias=False):
        '''
        Draw text with the given parameters on the given surface.

        surface - Surface to draw the text onto.

        fontName - Font name that identifies what font to use to draw the text.
        This font name must have been specified in the cFontManager

        rectOrPosToDrawTo - Where to render the text at.  This can be a 2
        item tuple or a Rect.  If a position tuple is used, the align
        arguments will be ignored.

        color - Color to draw the text with.

        alignHoriz - Specifies horizontal alignment of the text in the
        rectOrPosToDrawTo Rect.  If rectOrPosToDrawTo is not a Rect, the
        alignment is ignored.

        alignVert - Specifies vertical alignment of the text in the
        rectOrPosToDrawTo Rect.  If rectOrPosToDrawTo is not a Rect, the
        alignment is ignored.

        antialias - Whether to draw the text anti-aliased or not.
        '''
        font_name = None
        pair = (font_name, size)
        assert pair in self._fontDict, \
            'Font: %s Size: %d is not available in cFontManager.' % pair
        fontSurface = self._fontDict[(font_name, size)].render(text,
                                                               anti_alias, color)
        if isinstance(rect_or_pos_to_draw_to, tuple):
            surface.blit(fontSurface, rect_or_pos_to_draw_to)
        elif isinstance(rect_or_pos_to_draw_to, pygame.Rect):
            fontRect = fontSurface.get_rect()
            # align horiz
            if align_horiz == 'center':
                fontRect.centerx = rect_or_pos_to_draw_to.centerx
            elif align_horiz == 'right':
                fontRect.right = rect_or_pos_to_draw_to.right
            else:
                fontRect.x = rect_or_pos_to_draw_to.x  # left
            # align vert
            if align_vert == 'center':
                fontRect.centery = rect_or_pos_to_draw_to.centery
            elif align_vert == 'bottom':
                fontRect.bottom = rect_or_pos_to_draw_to.bottom
            else:
                fontRect.y = rect_or_pos_to_draw_to.y  # top

            surface.blit(fontSurface, fontRect)

def RunDemo():
    '''A simple demo of the use of the cFontManager class'''
    pygame.init()
    pygame.display.set_mode((640, 480))
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    # a font of None means to use the default font
    font_mgr = font_manager(((None, 24), (None, 48), ('arial', 24)))

    do_quit = False
    while not do_quit:
        clock.tick(60) # run at 60 fps
        screen.fill((0, 0, 0))

        white = (255, 255, 255)
        gray = (64, 64, 64)
        font_mgr.Draw(screen, None, 48, 'Default font, 48', (0, 50), white)
        font_mgr.Draw(screen, None, 24, 'Default font, 24', (0, 0), white)

        rect = pygame.Rect(0, 100, 640, 60)
        pygame.draw.rect(screen, gray, rect)
        font_mgr.Draw(screen, 'arial', 24, 'Arial 24 top left', rect, white, 'left', 'top')
        rect.top += 75

        pygame.draw.rect(screen, gray, rect)
        font_mgr.Draw(screen, 'arial', 24, 'Arial 24 centered', rect, white, 'center', 'center')
        rect.top += 75

        pygame.draw.rect(screen, gray, rect)
        font_mgr.Draw(screen, 'arial', 24, 'Arial 24 bottom right', rect, white, 'right', 'bottom')
        rect.top += 75

        pygame.draw.rect(screen, gray, rect)
        font_mgr.Draw(screen, 'arial', 24, 'Arial 24 left center, anti-aliased', rect, white, 'left', 'center', True)
        rect.top += 75

        pygame.display.update()
        if QUIT in [event.type for event in pygame.event.get()]:
            do_quit = True
    pygame.quit()

if __name__ == '__main__':
    # Execute the demo code if this file is run directly from the command line.
    # Do not run demo if file is imported.
    RunDemo()
