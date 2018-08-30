---
title: "Add-on settings & actions"
date: 2018-07-26T15:50:04-06:00
weight: 30
---

Artwork Beef configuration and manual actions when run from "Program Add-ons".

## General

#### "Add artwork for new videos / music after library updates"

The main process of Artwork Beef. Runs after library updates to add extended artwork for media items
newly added to the Kodi library, either from the file system or web services. Video and music
are configured separately. A media item is only "new" once, after it has been scanned it is no longer
"new".

##### "Update artwork for old items daily"

Check old items for new artwork. "Old" in this case refers to media items that have been in the
library for a while already. 4 months for newly released media that is still missing a bit of
artwork, 8 months otherwise. If the options "only identify local files" is enabled then
local files are checked monthly.

#### "Delete deselected artwork files"

Manually deselecting artwork like fanart will delete the original file. Otherwise the image will
stay in the file system and Artwork Beef will add it back to the library the next time this item
is scanned.

#### "Recycle deleted and replaced artwork files to temp/cache directory"

Recycled artwork goes to Kodi's local temp or cache directory.

#### "Disable/Enable Artwork Beef context items (per skin)

Hide the two context items under the "Manage" menu of the context menu of most media items.

### Sorting and auto filters

#### "Prefer 'fanart' with no title"

#### "Preferred artwork size"

Artwork larger than this will be sorted based on rating instead of size, and the minimum
size of artwork automatically added is adjusted.

#### "Minimum image rating"

Slider to set minimum image rating to be added automatically.

#### "Override image language (defaults to Kodi interface)"

#### "Prefer 'poster' with no title"

Save 'keyart' (aka textless poster) to 'poster' if available.

#### Action "Show latest artwork report"

Contains details on the latest automatic and manual processing Artwork Beef performed.

## TV Shows / Movies / Music videos / Music

Each media section is configurable separately, but the options are mostly the same.
Music only works for Kodi 18 Leia.

#### "Do not automatically add artwork from web services, only identify local files"

If you manage all of you media info with an external media manager, then you probably want this.
Manual artwork selection will still be able to pick artwork from web services, but only the
file system will be checked during automatic processing.

#### "Prefer artwork from specific web service"

Artwork from the specified web service will sort first for automatic and manual processing.
For artwork types that can have multiple images, automatic processing will _only_ include images from this
web service if any are available, to avoid picking duplicates from multiple sources automatically.

#### "Automatically add these artwork types from web services and file system"

A list of switches and number sliders for each art type for each individual media type to be
automatically added to the media library from web services and the file system. Some skins can work
with multiple artwork of the same type, like "fanart", which is configured with a number slider.
If you want other artwork types in the file system added to the Kodi library, include the artwork
type in the box "Additional art types for ... (comma separated)".

Artwork Beef will not automatically apply these changes to existing items in the library, you will need
to run "add missing artwork for ..." "all videos" or music to look for newly configured artwork.

You probably don't want "animatedposter" and "animatedfanart" in the "Additional art types" list,
that will conflict with Skin Helper Service.

##### "Select series for episode 'fanart'..."

Episode fanart must be enabled per series as they add a bundle of new API calls and just won't be
available for many series.

#### "Download these artwork types to the local file system"

Artwork types here will be downloaded to the local file system (generally next to the media items),
rather than linked directly to the original URL. This makes it easy to share with other Kodi installations
and saves a bundle of bandwidth for you and the web services. It is awkward to configure but I
suggest you enable it for everything (except maybe episode 'thumb'). For artwork types that can
have multiple images, only the base art name is needed; "fanart" will also include "fanart1", "fanart2",
"fanart3", etc if added to Kodi's library.

## Advanced

#### "TV show scraper (if source unknown)"

Kodi Jarvis (and early Krypton scrapers) didn't identify `uniqueid` sources for TV shows, this
setting will be used as a backup. 'tvdb' for TheTVDB or 'tmdb' for TheMovieDB.

#### "fanart.tv personal API key"

Set the **personal** API for fanart.tv, which reduces the delay for new artwork results from fanart.tv.
This is the API key that individual users of Artwork Beef (and other apps like it) should register for.

#### "Include detailed per item changes in the report"

Include more details for each processed media item in the "artwork report" file.

#### "Progress display for automatic processing"

"full progress bar" displays a persistent progress bar like Kodi's built in library updates can,
and it includes a count of updated artwork at the end. "just warnings and errors" only shows
notifications for warnings such as an error encountered accessing a web service or the add-on
crashes. Finally there is "only add-on crashes".

#### "Show final artwork update count notification"

Shows the final artwork update count in a notification. Overrides the count at the end of the
"full progress bar".

#### "Automatically preload local video / music library artwork to Kodi texture cache"

Artwork can be preloaded to the Kodi cache for faster browsing of new media. Video and music
are configured separately. Only works for artwork saved locally: if you are going to download
all artwork immediately for caching, then you might as well save it somewhere so you won't
have to download it again later.

#### "Manually select multiple images for all media types"

Allows manual selection of multiple images for all artwork. Mostly for skin designers or developers to
tinker with, it requires a skin or other interface or add-on to support multiple in some way.

### Files

#### "Replace episode / movie / music video 'thumb' with Kodi generated thumb"

Episode 'thumb' from web services are usually not great, and for movies it's not "extrathumbs"
but at least there is one. Separate config for each media type.

#### "Process movie set artwork in a central directory"

Save movie collection artwork to a central directory. Details on the
[Image files page]({{< ref "usage/fromfiles.md#movie-collection-artwork" >}}).

##### "central information directory"

#### "Grab movie set artwork from movie parent directory"

Mutually exclusive with "movie set central directory", but probably shouldn't be.

#### "Save movie / music video artwork with movie base file name"

Save movie artwork to "[movie name]-fanart.jpg" rather than "fanart.jpg".
Movies and music videos are configured separately.

#### "Save additional movie and TV show fanart to 'extrafanart' directory instead"

By default Artwork Beef saves extra fanart as "fanart1.jpg", "fanart2.jpg", and so on
next to the regular fanart. This instead saves them to the classic "extrafanart" directory.

#### "Save additional music video fanart to 'extrafanart' directory instead"

#### "Identify alternative Artwork Downloader and MSAA artwork files"

Like "logo.png" to "clearlogo". This is generally safe to leave enabled, it's an option in
case you _really_ do want the artwork saved to the Kodi library as "logo", which is rare at this
point.

### "In case of emergency"

These are for project API keys for the individual web services. You should generally not change
these, they are intended for the single built-in key to be used by all users of a single project / application.
These options are only provided for the future case that the built-in keys are disabled by the
web services after being ripped off.

# Actions

When run from "Program Add-ons", Artwork Beef can perform a number of actions.

- **"add missing artwork for ..."**
  - new videos / music
     - New media in the respective library. This is the same process that is run automatically
       after a Kodi library update.
  - old videos / music
     - Old media items in the library, as defined above. This is the same process that is run
       automatically after a Kodi library update but always includes old items.
  - all videos / music
     - All media items in the library. Don't run this very often, but it is here if you need it.
- **"identify unmatched movie sets with TMDb ..."**
  - Movie sets have to be matched by name rather than an exact ID like most other media types,
    so sometimes it needs a little help. This will display a list of all movie sets that have
    not yet been matched, and select one to enter a new name to search for.
- **"identify unmatched music videos with TheAudioDB ..."**
  - Just like movie sets, but match on "Artist Name - Song title".
- **"Remove artwork for media type ..."**
  - Remove a specific type of art for one specific type of media in the library. Doesn't touch
    local files.
  - Can also remove all artwork types that don't match the add-on configuration.
- **"Download existing remote images in the video library"**
  - Downloads existing images in the video library that aren't already saved locally.
  - Only works for the video library.
- **"Preload local video / music library artwork to texture cache"**
  - Preload local artwork to Kodi's device-local texture cache. Browsing the media library is
    faster with artwork cached.
  - Only works for local artwork. If you are going to download all artwork immediately for caching,
    then you might as well save it somewhere so you won't have to download it again later. Run
    "Download existing remote images in the video library" to set that up.