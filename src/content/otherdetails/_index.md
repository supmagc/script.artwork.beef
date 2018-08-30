---
title: "Problems and other questions"
date: 2018-03-22T18:00:25-07:00
weight: 2
---

#### What exactly does this do, why is it necessary?

Artwork Beef's main contributions to your Kodi setup is to add extended artwork to Kodi's library
and to download artwork from web services to the local file system. It is generally designed to
work automatically much like scrapers.

##### Add extended artwork to Kodi's library

Kodi and scrapers have had some support for extended artwork for awhile, but they aren't supported
to the same extent as basic artwork, like "poster" and "fanart", and need Artwork Beef or something
like it to add extended artwork to Kodi's library with JSON-RPC.

**Kodi 17 Krypton** and below only assigns basic artwork from scrapers, NFO files, and the
local file system. More help is needed to get any extended artwork into the library, whether you
already have them saved locally or want to "scrape" them from web services.

**Kodi 18 Leia** has added the ability to assign extended artwork from scrapers and NFO files.
It is still early days for Kodi 18 however, and not all scrapers currently
support extended artwork or they may not support the full selection.

Additionally for movie set artwork, Kodi just copies movie artwork, more help is needed
to add meaningfully different artwork for them.

##### Download artwork locally

Artwork Beef can download artwork locally to avoid troubles when web service URLs change, and
avoid redownloading the same image for multiple Kodi installations or in the future if the image
is no longer in Kodi's texture cache.

#### How do I quick-start this thing?

- The quickest way to get started is to install it and [configure]({{< ref "usage/settings.md" >}})
  it to your liking.
- If you want Artwork Beef to automatically add artwork for new media ...
    - Enable the setting "Add artwork for new videos after library updates" and / or
      "Add artwork for new music after library updates".
- If you want Artwork Beef to download image files to your local file system ...
    - Then add each image type to the settings "Download these artwork types to the local file system"
      for each media type at the bottom of the 'TV shows', 'Movies', 'Music videos', and 'Music' tabs.
- If you want Artwork Beef to only identify artwork you have already gathered
  [locally]({{< ref "usage/fromfiles.md" >}}) with a media manager ...
    - Enable the setting "Do not automatically add artwork from web services, only identify local files"
      at the top of each media tab.
- If you want Artwork Beef to ignore certain media types during automatic processing ...
    - Disable all options under "Automatically add these artwork types from web services and
      file system" and "Download these artwork types to the local file system" for that media type.
    - For movies, episodes, and music videos, also disable the options "Replace episode / movie /
      music video 'thumb' with Kodi generated thumb" on the Advanced tab.
- See [First usage]({{< ref "usage/firstusage.md" >}}) for more details.

#### I installed Artwork Beef but all my media items are still missing artwork!

Run Artwork Beef from "Program add-ons" and then "add missing artwork for ..." "new videos" or music.
Artwork Beef must be run on media items before it can do anything. It can be configured to run
automatically after library updates.

#### I see artwork for a movie set / collection / saga on fanart.tv but Artwork Beef won't show it.

Artwork Beef can only pull artwork from fanart.tv for movie sets that exist on TheMovieDB.
However, you can manually download that artwork and place it in the correct
[location on your file system]({{< ref "usage/fromfiles.md#movie-collection-artwork" >}}).
Then run "AB: add missing artwork" on the affected movie set.

#### I can't see artwork while browsing the library, but I do see it assigned in "AB: select artwork..." or Kodi's built-in "Choose art" dialog.

Artwork Beef has done its job. Skins are responsible for displaying artwork assigned in the
Kodi library. Are you sure you have configured the _skin_ to show the artwork type you expect
for the media type you are looking at?

#### Why don't I see new artwork I just submitted to a web service when manually selecting artwork?

- It may take a few days for new artwork to be available.
- Artwork Beef caches the previous image results from web services for 72 hours.

#### Images from web services are added to the library but are not visible.

Most likely the web service is temporarily/intermittently unavailable. Try again later.
Configuring Artwork Beef to download artwork to your local file system is probably a good idea.

#### Manual selection of artwork doesn't show any artwork from one or any web service.

1. Does it happen for all media items of a particular type?
    - If there is a message about "Invalid project API key" for a particular web service:
        - Either the built-in API keys have been disabled and you will have to sign up for a project
          key of your own;
        - Or you have entered your own project API key improperly and should remove that setting
          and try again.
    - Or maybe the web service is temporarily unavailable, or your Kodi device's internet connection
      is broken. The Kodi log and Artwork Beef's artwork report may have more details.
    - Otherwise post a reply on the forum thread with a description of the problem, a
      [Kodi debug log], and the latest group of artwork-report.txt.
2. Or just a handful of media items?
    - Artwork Beef requires web service IDs (like an IMDB number) in the Kodi library - except for
      movie sets and music videos. These should be included in NFO files, scrapers, or embedded tags.
        - If you use scrapers for the media item, make sure your scrapers are up to date and
          refresh the item.
        - If you have NFO files, make sure there is a "uniqueid" element in it.
          An "imdbnumber" element should also work (for movies and TV shows), and an "id" element might work.
          If your NFOs don't have these elements then upgrade your media manager and recreate the NFOs,
          then refresh the item in Kodi.
        - Music must be tagged with MusicBrainz IDs. Use MusicBrainz Picard for tagging files.

[Kodi debug log]: https://kodi.wiki/view/Debug-log

#### Artwork Beef cannot find artwork for some movie sets / collections from fanart.tv.

Artwork Beef must look up movie set artwork on fanart.tv by a TheMovieDB ID, which has
[different rules](https://www.themoviedb.org/bible/collection)
for what a movie collection is than you might. You can download the artwork and place it in the
file system manually, and Artwork Beef will add it to the library when the movie set is next scanned.

#### A Kodi skin or web interface is showing a thumbnail image instead of a movie poster.

The skin / web interface is pulling up the movie thumb and expecting the fallback poster,
but it should instead pick the poster first and fall back to the thumb only if the poster
doesn't exist. They are two different images for two different purposes and should be chosen
based on the interface design.

#### Where do I put my project API keys for other web services?

- At the bottom of the Advanced page of add-on settings.
- I do not suggest you do this, the option is only available in case the built-in project keys
  stop working.

#### Where is the option to replace the fanart slideshow from Artwork Downloader?

No such option is available, Artwork Beef will not duplicate image files for this purpose.
[Skins have other options] that don't require duplicating files.

[Skins have other options]: {{< ref "skins/addonfreefun.md#grab-random-fanart-plus-any-other-info-from-items-in-any-library-path" >}}