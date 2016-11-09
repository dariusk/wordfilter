module Paths_wordfilter where

import System.FilePath ((</>))

getDataFileName :: FilePath -> IO FilePath
getDataFileName = (return . ("lib" </>))
