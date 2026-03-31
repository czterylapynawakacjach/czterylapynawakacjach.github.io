import { ui, defaultLang } from './ui';

export function getLangFromUrl(url: URL) {
  const parts = url.pathname.split('/').filter(Boolean);
  
  // Case for /v1/pl/ or /v3/en/
  if (parts.length >= 2 && parts[0].startsWith('v') && !isNaN(parseInt(parts[0].substring(1)))) {
    const lang = parts[1];
    if (lang in ui) return lang as keyof typeof ui;
  }
  
  // Case for /pl/ or /en/
  const lang = parts[0];
  if (lang && lang in ui) return lang as keyof typeof ui;
  
  return defaultLang;
}

export function useTranslations(lang: keyof typeof ui) {
  return function t(key: keyof typeof ui[typeof defaultLang]) {
    return ui[lang][key] || ui[defaultLang][key];
  }
}

export function useTranslatedPath(lang: keyof typeof ui, version?: string) {
  return function translatePath(path: string, l: string = lang) {
    const vPrefix = version ? `/${version}` : '';
    const cleanPath = path.startsWith('/') ? path : '/' + path;
    // Special case for root paths
    if (path === '' || path === '/') {
        return `${vPrefix}/${l}/`;
    }
    return `${vPrefix}/${l}${cleanPath}`;
  }
}
