# SE Ranking API & MCP — Documentation Map (Citation Index)

This is the **source of truth for citations**. Every official link below was taken
from the live documentation sidebar at https://seranking.com/api.html. When you cite
a source, copy the URL **verbatim from this file** — do not invent anchors.

The docs are split into three top-level areas:

1. **API (general)** — access, credits, rate limits, integrations (incl. MCP), usage rules.
2. **Data API** — bulk research data (keywords, backlinks, domains, SERP, audits, AI search). Read-only research data, billed in API credits/units. Not tied to a tracked project.
3. **Project API** — manage and automate things *inside* a tracked SE Ranking project (rank tracking, keyword/competitor management, project-level audits, backlink monitor, AI Result Tracker).

> Disambiguation rule: several concepts exist in **both** Data and Project APIs
> (Website Audit, Backlinks/Backlink Checker, AI Search/AI Result Tracker).
> - "I have a tracked project / I want to manage keywords, competitors, prompts" → **Project API**.
> - "I want one-off bulk research on any domain/keyword without a project" → **Data API**.
> If the user is ambiguous, say which layer your answer assumes and cite that layer.

---

<!-- AUTO-GENERATED:START -- rewritten by scripts/refresh_doc_map.py on 2026-07-20. Do not edit by hand. -->

## 1. API (general)

### introduction

| Topic | URL |
|---|---|
| Introduction | https://seranking.com/api.html |

### how-to-get-api

| Topic | URL |
|---|---|
| Getting API access | https://seranking.com/api/how-to-get-api/ |

### api-credits-system

| Topic | URL |
|---|---|
| API credit system | https://seranking.com/api/api-credits-system/ |

### rate-limits

| Topic | URL |
|---|---|
| API rate limits | https://seranking.com/api/rate-limits/ |

### integrations

| Topic | URL |
|---|---|
| Integrations | https://seranking.com/api/integrations/ |
| Data Studio | https://seranking.com/api/integrations/data-studio/ |
| MCP | https://seranking.com/api/integrations/mcp/ |
| n8n | https://seranking.com/api/integrations/n8n |
| Make.com | https://seranking.com/api/integrations/make-com |

### usage-guidelines-for-commercial-purposes

| Topic | URL |
|---|---|
| Usage guidelines for commercial purposes | https://seranking.com/api/usage-guidelines-for-commercial-purposes/ |

### se-visible

| Topic | URL |
|---|---|
| Overview | https://seranking.com/api/se-visible/ |
| Getting started | https://seranking.com/api/se-visible/getting-started/ |
| Base URL | https://seranking.com/api/se-visible/getting-started#base-url |
| Authentication | https://seranking.com/api/se-visible/getting-started#authentication |
| Resource model | https://seranking.com/api/se-visible/getting-started#resource-model |
| Making requests | https://seranking.com/api/se-visible/getting-started#making-requests |
| Pagination | https://seranking.com/api/se-visible/getting-started#pagination |
| Filtering and array parameters | https://seranking.com/api/se-visible/getting-started#filtering-and-array-parameters |
| Date ranges and compare mode | https://seranking.com/api/se-visible/getting-started#date-ranges-and-compare-mode |
| Usage and limits | https://seranking.com/api/se-visible/getting-started#usage-and-limits |
| Errors | https://seranking.com/api/se-visible/getting-started#errors |
| Support | https://seranking.com/api/se-visible/getting-started#support |
| Projects | https://seranking.com/api/se-visible/projects/ |
| List projects | https://seranking.com/api/se-visible/projects#list-projects |
| Create project | https://seranking.com/api/se-visible/projects#create-project |
| Get project details | https://seranking.com/api/se-visible/projects#get-project-details |
| Delete a project | https://seranking.com/api/se-visible/projects#delete-a-project |
| Brands | https://seranking.com/api/se-visible/brands/ |
| List tracked brands | https://seranking.com/api/se-visible/brands#list-tracked-brands |
| Create competitor brand | https://seranking.com/api/se-visible/brands#create-competitor-brand |
| List mentioned brands | https://seranking.com/api/se-visible/brands#list-mentioned-brands |
| Get aggregated brand metrics | https://seranking.com/api/se-visible/brands#get-aggregated-brand-metrics |
| Update brand | https://seranking.com/api/se-visible/brands#update-brand |
| Delete brand | https://seranking.com/api/se-visible/brands#delete-brand |
| Add aliases to brand | https://seranking.com/api/se-visible/brands#add-aliases-to-brand |
| Topics | https://seranking.com/api/se-visible/topics/ |
| Create topics | https://seranking.com/api/se-visible/topics#create-topics |
| Update a topic title | https://seranking.com/api/se-visible/topics#update-a-topic-title |
| Delete a topic | https://seranking.com/api/se-visible/topics#delete-a-topic |
| Prompts | https://seranking.com/api/se-visible/prompts/ |
| List prompts or topics | https://seranking.com/api/se-visible/prompts#list-prompts-or-topics |
| Delete prompts | https://seranking.com/api/se-visible/prompts#delete-prompts |
| Create prompts for a topic | https://seranking.com/api/se-visible/prompts#create-prompts-for-a-topic |
| Move prompts to a topic | https://seranking.com/api/se-visible/prompts#move-prompts-to-a-topic |
| Get prompt details | https://seranking.com/api/se-visible/prompts#get-prompt-details |
| Get prompt result list | https://seranking.com/api/se-visible/prompts#get-prompt-result-list |
| Get prompt result details | https://seranking.com/api/se-visible/prompts#get-prompt-result-details |
| Download raw LLM response dump | https://seranking.com/api/se-visible/prompts#download-raw-llm-response-dump |
| Sources | https://seranking.com/api/se-visible/sources/ |
| Get project sources | https://seranking.com/api/se-visible/sources#get-project-sources |
| Reference | https://seranking.com/api/se-visible/reference/ |
| AI models | https://seranking.com/api/se-visible/reference#ai-models |
| Sentiment | https://seranking.com/api/se-visible/reference#sentiment |
| Project status | https://seranking.com/api/se-visible/reference#project-status |
| Country codes | https://seranking.com/api/se-visible/reference#country-codes |
| Language codes | https://seranking.com/api/se-visible/reference#language-codes |
| Source type | https://seranking.com/api/se-visible/reference#source-type |
| URL category types | https://seranking.com/api/se-visible/reference#url-category-types |
| Brand match mode | https://seranking.com/api/se-visible/reference#brand-match-mode |
| Prompt list grouping | https://seranking.com/api/se-visible/reference#prompt-list-grouping |
| Brand metrics dimensions and metrics | https://seranking.com/api/se-visible/reference#brand-metrics-dimensions-and-metrics |
| Sort fields | https://seranking.com/api/se-visible/reference#sort-fields |
| Date ranges and compare mode | https://seranking.com/api/se-visible/reference#date-ranges-and-compare-mode |
| Array parameters | https://seranking.com/api/se-visible/reference#array-parameters |
| Pagination | https://seranking.com/api/se-visible/reference#pagination |
| Error codes | https://seranking.com/api/se-visible/reference#error-codes |
| Authentication | https://seranking.com/api/se-visible/reference#authentication |
| Subscription | https://seranking.com/api/se-visible/subscription/ |
| Get subscription details | https://seranking.com/api/se-visible/subscription#get-subscription-details |

### integrations

| Topic | URL |
|---|---|
| Connect to n8n | https://seranking.com/api/integrations/n8n/ |
| Connect to Data Studio | https://seranking.com/api/integrations/data-studio/ |
| Connect to Make | https://seranking.com/api/integrations/make-com/ |

## 2. Data API

### data

| Topic | URL |
|---|---|
| Overview | https://seranking.com/api/data/ |

### getting-started

| Topic | URL |
|---|---|
| Getting started | https://seranking.com/api/data/getting-started/ |
| Authentication | https://seranking.com/api/data/getting-started#authentication |
| Making requests | https://seranking.com/api/data/getting-started#making-a-request |
| Postman collection | https://seranking.com/api/data/getting-started#postman-collection |
| Unit costs | https://seranking.com/api/data/getting-started#unit-costs |
| Plans and pricing | https://seranking.com/api/data/getting-started#plans-and-pricing |

### quickstarts

| Topic | URL |
|---|---|
| Quickstarts | https://seranking.com/api/data/quickstarts/ |
| Find keyword opportunities | https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/ |
| Assess AI search visibility | https://seranking.com/api/data/quickstarts/assess-ai-search-visibility/ |
| Retrieve URLs with SEO issues | https://seranking.com/api/data/quickstarts/retrieve-urls-affected-by-seo-issues/ |
| Use Website Audit API for SEO growth | https://seranking.com/api/data/quickstarts/use-website-audit-api-to-grow-rankings-and-traffic/ |
| Generate reports with SEOIntel | https://seranking.com/api/data/quickstarts/generate-seo-intelligence-reports-with-seointel/ |
| Build authority with link building | https://seranking.com/api/data/quickstarts/build-authority-with-link-building/ |
| Analyze domain traffic & competitors | https://seranking.com/api/data/quickstarts/analyze-domain-traffic-top-markets-and-competitors/ |

### backlinks

| Topic | URL |
|---|---|
| Backlinks | https://seranking.com/api/data/backlinks/ |
| Get backlink summary | https://seranking.com/api/data/backlinks#summary |
| Get backlink metrics | https://seranking.com/api/data/backlinks#metrics |
| List all backlinks | https://seranking.com/api/data/backlinks#all |
| Fetch backlinks in batches | https://seranking.com/api/data/backlinks#raw |
| Get total backlinks count | https://seranking.com/api/data/backlinks#count |
| Export backlinks data | https://seranking.com/api/data/backlinks#export |
| List new/lost backlinks | https://seranking.com/api/data/backlinks#history |
| Get daily new/lost backlinks | https://seranking.com/api/data/backlinks#history-count |
| Get cumulative backlinks | https://seranking.com/api/data/backlinks#history-cumulative |
| Get backlink anchor texts | https://seranking.com/api/data/backlinks#anchors |
| List referring domains | https://seranking.com/api/data/backlinks#refdomains |
| Get referring domains count | https://seranking.com/api/data/backlinks#refdomains-count |
| List new/lost referring domains | https://seranking.com/api/data/backlinks#refdomains-history |
| Get daily new/lost referring domains | https://seranking.com/api/data/backlinks#refdomains-history-count |
| List referring IPs | https://seranking.com/api/data/backlinks#referring-ips |
| Get total referring IPs count | https://seranking.com/api/data/backlinks#referring-ips-count |
| Get total referring subnets count | https://seranking.com/api/data/backlinks#referring-subnets-count |
| List pages with backlinks | https://seranking.com/api/data/backlinks#indexed-pages |
| Get page/domain authority | https://seranking.com/api/data/backlinks#authority |
| Get domain authority | https://seranking.com/api/data/backlinks#authority-domain |
| Get domain authority distribution | https://seranking.com/api/data/backlinks#authority-domain-distribution |
| Get domain authority history | https://seranking.com/api/data/backlinks/#authority-domain-history |
| Get page authority | https://seranking.com/api/data/backlinks#authority-page |
| Get page authority history | https://seranking.com/api/data/backlinks#authority-page-history |

### domain-analysis

| Topic | URL |
|---|---|
| Domain Analysis | https://seranking.com/api/data/domain-analysis/ |
| Get domain overview by region | https://seranking.com/api/data/domain-analysis#regional-database |
| Get worldwide domain overview | https://seranking.com/api/data/domain-analysis#worldwide-aggregate |
| Get worldwide URL overview | https://seranking.com/api/data/domain-analysis/#worldwide-aggregate-url |
| Get traffic/keyword history | https://seranking.com/api/data/domain-analysis#history-trends |
| Get keyword rankings | https://seranking.com/api/data/domain-analysis#domain-keywords |
| Get domain pages | https://seranking.com/api/data/domain-analysis/#domain-pages |
| Get domain subdomains | https://seranking.com/api/data/domain-analysis/#domain-subdomains |
| Get paid ads by keyword | https://seranking.com/api/data/domain-analysis#paid-ads-keyword |
| Get paid ads for domain | https://seranking.com/api/data/domain-analysis#paid-ads-domain |
| Get domain competitors | https://seranking.com/api/data/domain-analysis#competitors |
| Analyze keyword overlap/gaps | https://seranking.com/api/data/domain-analysis#domain-comparison |

### keyword-research

| Topic | URL |
|---|---|
| Keyword Research | https://seranking.com/api/data/keyword-research/ |
| Get Keywords metrics | https://seranking.com/api/data/keyword-research#export |
| Get similar keywords | https://seranking.com/api/data/keyword-research#similar |
| Get related keywords | https://seranking.com/api/data/keyword-research#related |
| Get question keywords | https://seranking.com/api/data/keyword-research#questions |
| Get longtail keywords | https://seranking.com/api/data/keyword-research#longtail |

### ai-search

| Topic | URL |
|---|---|
| AI Search | https://seranking.com/api/data/ai-search |
| Get AI search overview | https://seranking.com/api/data/ai-search#overview |
| Get AI search leaderboard | https://seranking.com/api/data/ai-search/#leaderboard |
| Discover brand by URL | https://seranking.com/api/data/ai-search#discover-brand-by-url |
| Get prompts by brand | https://seranking.com/api/data/ai-search#get-prompts-by-brand |
| Get prompts by target | https://seranking.com/api/data/ai-search#get-prompts-by-target |
| Filtering results | https://seranking.com/api/data/ai-search#filtering-results |

### website-audit

| Topic | URL |
|---|---|
| Website Audit | https://seranking.com/api/data/website-audit/ |
| Create audit | https://seranking.com/api/data/website-audit#create-audit |
| List audits | https://seranking.com/api/data/website-audit#list-audits |
| Get audit status | https://seranking.com/api/data/website-audit#get-audit-status |
| Get audit report | https://seranking.com/api/data/website-audit#get-audit-report |
| Get all crawled pages | https://seranking.com/api/data/website-audit#get-all-crawled-pages |
| Get audit pages by issue | https://seranking.com/api/data/website-audit#get-audit-pages-by-issue |
| Get all issues by URL | https://seranking.com/api/data/website-audit#get-all-issues-for-a-specific-url |
| Get all found links | https://seranking.com/api/data/website-audit#get-all-found-links |
| Get audit by date | https://seranking.com/api/data/website-audit#get-audit-history-by-date |
| Update audit title | https://seranking.com/api/data/website-audit#update-audit-title |
| Delete audit | https://seranking.com/api/data/website-audit#delete-audit |
| Recheck audit | https://seranking.com/api/data/website-audit#recheck-audit |

### account-system

| Topic | URL |
|---|---|
| Account System | https://seranking.com/api/data/account-system/ |
| Get subscription details | https://seranking.com/api/data/account-system/#subscription |

### reference

| Topic | URL |
|---|---|
| Reference | https://seranking.com/api/data/reference |
| Glossary | https://seranking.com/api/data/reference#glossary |
| Regional codes | https://seranking.com/api/data/reference#regional-database-codes |
| SERP features | https://seranking.com/api/data/reference#serp-features |
| Site Audit issue codes | https://seranking.com/api/data/reference/#site-audit-issue-codes |
| Error handling | https://seranking.com/api/data/reference#error-handling |

### quickstarts

| Topic | URL |
|---|---|
| Follow the guide | https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/ |
| Follow the guide | https://seranking.com/api/data/quickstarts/assess-ai-search-visibility/ |
| Follow the guide | https://seranking.com/api/data/quickstarts/retrieve-urls-affected-by-seo-issues/ |
| Follow the guide | https://seranking.com/api/data/quickstarts/build-authority-with-link-building/ |
| Follow the guide | https://seranking.com/api/data/quickstarts/analyze-domain-traffic-top-markets-and-competitors/ |
| Follow the guide | https://seranking.com/api/data/quickstarts/use-website-audit-api-to-grow-rankings-and-traffic/ |

### website-audit

| Topic | URL |
|---|---|
| View docs | https://seranking.com/api/data/website-audit/ |

### ai-search

| Topic | URL |
|---|---|
| View docs | https://seranking.com/api/data/ai-search/ |

## 3. Project API

### project

| Topic | URL |
|---|---|
| Overview | https://seranking.com/api/project/ |

### getting-started

| Topic | URL |
|---|---|
| Getting started | https://seranking.com/api/project/getting-started/ |
| API access and keys | https://seranking.com/api/project/getting-started#api-access-keys |
| Making requests | https://seranking.com/api/project/getting-started#making-requests |
| Rate limits | https://seranking.com/api/project/getting-started#rate-limits-quotas |
| Error handling | https://seranking.com/api/project/getting-started#error-handling |

### project-management

| Topic | URL |
|---|---|
| Project Management | https://seranking.com/api/project/project-management/ |
| List projects | https://seranking.com/api/project/project-management#list-projects |
| List project search engines | https://seranking.com/api/project/project-management#list-project-search-engines |
| Add search engine to project | https://seranking.com/api/project/project-management/#add-search-engine-to-project |
| Change search engine in project | https://seranking.com/api/project/project-management#change-search-engine-in-project |
| Delete search engine from project | https://seranking.com/api/project/project-management#delete-search-engine-from-project |
| List website keywords | https://seranking.com/api/project/project-management#website-keyword-list |
| Get project summary statistics | https://seranking.com/api/project/project-management#summary-statistics |
| Get keyword statistics | https://seranking.com/api/project/project-management#keyword-statistics |
| Get total number of ads chart | https://seranking.com/api/project/project-management#total-number-of-ads-chart |
| Get historical dates | https://seranking.com/api/project/project-management#historical-dates |
| Add keywords to project | https://seranking.com/api/project/project-management#add-queries-to-project |
| Add project | https://seranking.com/api/project/project-management#adding-a-project |
| Change project settings | https://seranking.com/api/project/project-management#change-project-settings |
| Delete project | https://seranking.com/api/project/project-management#delete-project |
| Delete keywords | https://seranking.com/api/project/project-management#delete-keywords |
| Set manual keyword position | https://seranking.com/api/project/project-management#set-manual-position |
| Run position check | https://seranking.com/api/project/project-management#run-position-check |

### project-groups

| Topic | URL |
|---|---|
| Project Groups | https://seranking.com/api/project/project-groups/ |
| Add project group | https://seranking.com/api/project/project-groups#add-project-group |
| Rename project group | https://seranking.com/api/project/project-groups#rename-project-group |
| Delete project group | https://seranking.com/api/project/project-groups#delete-project-group |
| List project groups | https://seranking.com/api/project/project-groups#project-group-list |
| Move projects to project group | https://seranking.com/api/project/project-groups#move-projects-to-project-group |

### keyword-groups

| Topic | URL |
|---|---|
| Keyword Groups | https://seranking.com/api/project/keyword-groups/ |
| Add keyword group | https://seranking.com/api/project/keyword-groups#add-keyword-group |
| Move keywords to another group | https://seranking.com/api/project/keyword-groups#move-keywords-to-another-group |
| Rename keyword group | https://seranking.com/api/project/keyword-groups#rename-keyword-group |
| Delete keyword group | https://seranking.com/api/project/keyword-groups#delete-keyword-group |
| List keyword groups | https://seranking.com/api/project/keyword-groups#list-keyword-groups |

### competitors

| Topic | URL |
|---|---|
| Competitors | https://seranking.com/api/project/competitors/ |
| Add competitor | https://seranking.com/api/project/competitors#add-competitor |
| List competitors | https://seranking.com/api/project/competitors#list-competitors |
| Get competitor keyword positions | https://seranking.com/api/project/competitors#get-competitor-keyword-positions |
| Delete competitor | https://seranking.com/api/project/competitors#delete-competitor |
| Get TOP 10 results | https://seranking.com/api/project/competitors#get-top-10-results |
| Get TOP 100 results | https://seranking.com/api/project/competitors#get-top-100-results |
| Get all competitors | https://seranking.com/api/project/competitors#get-all-competitors |

### url-tags

| Topic | URL |
|---|---|
| URL Tags | https://seranking.com/api/project/url-tags/ |
| List tags | https://seranking.com/api/project/url-tags#list-tags |
| Add tag | https://seranking.com/api/project/url-tags#add-tag |
| Update tag assignment | https://seranking.com/api/project/url-tags#update-tag-assignment |
| Delete tag | https://seranking.com/api/project/url-tags#delete-tag |

### analytics-traffic

| Topic | URL |
|---|---|
| Analytics Traffic | https://seranking.com/api/project/analytics-traffic/ |
| Get Google Search Console data | https://seranking.com/api/project/analytics-traffic#google-search-console-data |
| Calculate SEO potential | https://seranking.com/api/project/analytics-traffic#seo-potential |

### account-management

| Topic | URL |
|---|---|
| Account Management | https://seranking.com/api/project/account-management/ |
| Get user profile | https://seranking.com/api/project/account-management/#get-user-profile |
| List sub-accounts | https://seranking.com/api/project/account-management#list-sub-accounts |
| Create sub-account | https://seranking.com/api/project/account-management#create-sub-account |
| Get sub-account details | https://seranking.com/api/project/account-management#/api/project/sub-account-management#get-sub-account-details |
| Delete sub-account | https://seranking.com/api/project/account-management#delete-sub-account |
| Update sub-account | https://seranking.com/api/project/account-management#update-sub-account |
| List shared projects | https://seranking.com/api/project/account-management#list-shared-projects |
| List owned projects | https://seranking.com/api/project/account-management#list-owned-projects |
| Share project with sub-account | https://seranking.com/api/project/account-management#share-projects-with-sub-account |

### general-data

| Topic | URL |
|---|---|
| General Data | https://seranking.com/api/project/general-data/ |
| List search engines | https://seranking.com/api/project/general-data#list-search-engines |
| List languages for Google | https://seranking.com/api/project/general-data#list-languages-for-google |
| List regions to get search volume | https://seranking.com/api/project/general-data#list-regions-to-get-search-volume |
| Get keyword search volume | https://seranking.com/api/project/general-data#get-keyword-search-volume |

### marketing-plan

| Topic | URL |
|---|---|
| Marketing Plan | https://seranking.com/api/project/marketing-plan/ |
| List plan items | https://seranking.com/api/project/marketing-plan#list-plan-items |
| Add task | https://seranking.com/api/project/marketing-plan#add-task |
| Update task | https://seranking.com/api/project/marketing-plan#update-task |
| Delete task | https://seranking.com/api/project/marketing-plan#delete-task |
| Set task status | https://seranking.com/api/project/marketing-plan#set-task-status |

### audit

| Topic | URL |
|---|---|
| Website Audit | https://seranking.com/api/project/audit/ |
| Create audit | https://seranking.com/api/project/audit#create-audit |
| List audits | https://seranking.com/api/project/audit#list-audits |
| Get audit status | https://seranking.com/api/project/audit#get-audit-status |
| Get audit report | https://seranking.com/api/project/audit#get-audit-report |
| Get all crawled pages | https://seranking.com/api/project/audit#get-all-crawled-pages |
| Get audit pages by issue | https://seranking.com/api/project/audit#get-audit-pages-by-issue |
| Get all issues for URL | https://seranking.com/api/project/audit#get-all-issues-for-url |
| Get all links | https://seranking.com/api/project/audit#get-all-links |
| Get audit history | https://seranking.com/api/project/audit#get-audit-history |
| Update audit title | https://seranking.com/api/project/audit#update-audit-title |
| Delete audit | https://seranking.com/api/project/audit#delete-audit |
| Recheck audit | https://seranking.com/api/project/audit#recheck-audit |

### backlink-checker

| Topic | URL |
|---|---|
| Backlink Checker | https://seranking.com/api/project/backlink-checker/ |
| List backlinks | https://seranking.com/api/project/backlink-checker#list-backlinks |
| Add backlink | https://seranking.com/api/project/backlink-checker#add-backlink |
| Import backlinks list | https://seranking.com/api/project/backlink-checker#import-backlinks-list |
| Update backlink import settings | https://seranking.com/api/project/backlink-checker#update-backlink-import-settings |
| Start backlink import from Google Search Console | https://seranking.com/api/project/backlink-checker#start-backlink-import-from-google-search-console |
| Get backlink import status from Google Search Console | https://seranking.com/api/project/backlink-checker#get-backlink-import-status-from-google-search-console |
| Delete backlinks | https://seranking.com/api/project/backlink-checker#delete-backlinks |
| Recheck backlinks | https://seranking.com/api/project/backlink-checker#recheck-backlinks |
| Get backlink statistics | https://seranking.com/api/project/backlink-checker#get-backlink-statistics |
| List disavowed backlinks | https://seranking.com/api/project/backlink-checker#list-disavowed-backlinks |
| Add disavowed backlinks | https://seranking.com/api/project/backlink-checker#add-disavowed-backlinks |
| Delete disavowed backlink | https://seranking.com/api/project/backlink-checker#delete-disavowed-backlink |
| List backlink groups | https://seranking.com/api/project/backlink-checker#list-backlink-groups |
| Create backlink group | https://seranking.com/api/project/backlink-checker#create-backlink-group |
| Delete backlink group | https://seranking.com/api/project/backlink-checker#delete-backlink-group |
| Rename backlink group | https://seranking.com/api/project/backlink-checker#rename-backlink-group |
| Move backlinks to group | https://seranking.com/api/project/backlink-checker#move-backlinks-to-group |

### ai-result-tracker

| Topic | URL |
|---|---|
| AI Results Tracker | https://seranking.com/api/project/ai-result-tracker/ |
| Get site brand | https://seranking.com/api/project/ai-result-tracker/#get-brands |
| Save site brand | https://seranking.com/api/project/ai-result-tracker/#save-brands |
| List LLM engines | https://seranking.com/api/project/ai-result-tracker/#list-llm |
| Get LLM engine | https://seranking.com/api/project/ai-result-tracker/#get-llm |
| Create LLM engine | https://seranking.com/api/project/ai-result-tracker/#create-llm |
| Update LLM engine | https://seranking.com/api/project/ai-result-tracker/#update-llm |
| Delete LLM engine | https://seranking.com/api/project/ai-result-tracker/#delete-llm |
| Get LLM status | https://seranking.com/api/project/ai-result-tracker/#llm-status |
| Get LLM statistics | https://seranking.com/api/project/ai-result-tracker/#llm-statistics |
| List prompts | https://seranking.com/api/project/ai-result-tracker/#get-prompts |
| Add prompts | https://seranking.com/api/project/ai-result-tracker/#add-prompts |
| Delete prompts | https://seranking.com/api/project/ai-result-tracker/#delete-prompts |
| Get prompt answer | https://seranking.com/api/project/ai-result-tracker#get-answer |
| Get prompt rankings | https://seranking.com/api/project/ai-result-tracker/#get-rankings |

### airt-sources

| Topic | URL |
|---|---|
| AIRT Sources | https://seranking.com/api/project/airt-sources/ |
| Get sources summary | https://seranking.com/api/project/airt-sources#get-sources-summary |
| List source domains | https://seranking.com/api/project/airt-sources#list-source-domains |
| List source pages | https://seranking.com/api/project/airt-sources#list-source-pages |
| Get sources recommendations | https://seranking.com/api/project/airt-sources#get-sources-recommendations |

### airt-competitors

| Topic | URL |
|---|---|
| AIRT Competitors | https://seranking.com/api/project/airt-competitors/ |
| Get competitors breakdown | https://seranking.com/api/project/airt-competitors#get-competitors-breakdown |
| Get competitors check dates | https://seranking.com/api/project/airt-competitors#get-competitors-check-dates |
| Get source metrics | https://seranking.com/api/project/airt-competitors#get-source-metrics |

### airt-groups

| Topic | URL |
|---|---|
| AIRT Groups | https://seranking.com/api/project/airt-groups/ |
| List prompt groups | https://seranking.com/api/project/airt-groups#list-prompt-groups |
| Create prompt group | https://seranking.com/api/project/airt-groups#create-prompt-group |
| Rename prompt group | https://seranking.com/api/project/airt-groups#rename-prompt-group |
| Delete prompt group | https://seranking.com/api/project/airt-groups#delete-prompt-group |
| Change group order | https://seranking.com/api/project/airt-groups#change-group-order |
| Delete all prompts in group | https://seranking.com/api/project/airt-groups#delete-all-prompts-in-group |
| Move prompts to group | https://seranking.com/api/project/airt-groups#move-prompts-to-group |
| Move all prompts from one group to another | https://seranking.com/api/project/airt-groups#move-all-prompts-from-one-group-to-another |

### project

| Topic | URL |
|---|---|
| View docs | https://seranking.com/api/project/ |

<!-- AUTO-GENERATED:END -->

---

## Quick keyword → section router

Use this to jump fast. If a term matches both layers, see the disambiguation rule at the top.

- **API key / where do I get access / token** → API: Getting API access
- **credits / units / how much does a call cost / pricing** → API credit system; Data getting-started → Unit costs / Plans and pricing
- **rate limit / requests per second / 429 / quota** → API rate limits; per-layer Getting started
- **MCP / connect Claude / Cursor / ChatGPT connector / plain-language queries** → MCP integration
- **n8n / Make / Data Studio / Looker** → Integrations subsection
- **auth / authentication / how do I sign requests** → Data or Project Getting started → Authentication
- **error / status code / handling failures** → Data Reference → Error handling; Project Getting started → Error handling
- **region codes / country codes / glossary / SERP features / issue codes** → Data Reference
- **keyword volume / difficulty / CPC / similar / related / questions / longtail** → Data Keyword Research (research) OR Project General Data (volume within project)
- **backlinks for any domain / anchors / referring domains / authority (research)** → Data Backlinks
- **manage backlinks in my project / disavow / import / GSC import** → Project Backlink Checker
- **domain overview / traffic / competitors / keyword gap (research)** → Data Domain Analysis
- **rank tracking / positions / add keywords to project / run position check** → Project Project Management
- **website audit (one-off any site)** → Data Website Audit
- **website audit (inside my project)** → Project Website Audit
- **AI visibility / brand mentions / share of voice / prompts (research, any brand)** → Data AI Search
- **track my brand across LLMs / prompts / LLM engines in my project** → Project AI Result Tracker (+ AIRT Groups)
- **GSC data / SEO potential** → Project Analytics Traffic
- **sub-accounts / share projects / user profile** → Project Account Management
- **subscription details (Data layer)** → Data Account System
