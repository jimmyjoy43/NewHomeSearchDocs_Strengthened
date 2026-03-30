import csv, json, os
from pathlib import Path

DATE = '2026-03-22'
BASE = Path('/mnt/data')
OUT = BASE / 'building_packets'
OUT.mkdir(exist_ok=True)

with open(BASE / 'buildings.csv', newline='') as f:
    buildings = {row['building_id']: row for row in csv.DictReader(f)}


def ev(scope_id, criterion, claim, source_type, source_name, source_url, evidence_class, sentiment, note):
    return {
        'evidence_id': '',
        'scope_type': 'building',
        'scope_id': scope_id,
        'criterion': criterion,
        'claim': claim,
        'source_type': source_type,
        'source_name': source_name,
        'source_url': source_url,
        'retrieved_date': DATE,
        'evidence_class': evidence_class,
        'sentiment': sentiment,
        'quote_or_note': note,
    }

cfg = {
    '1600-vine-1600-vine-st': {
        'management_company': 'Sentral',
        'quiet_score': '2', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '1', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '2', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'medium',
        'pricing_risk': 'medium',
        'status': 'rejected',
        'open_questions': '',
        'notes': 'Hard stop kept. Official amenity evidence remains strong, but repo history plus the Hollywood/Vine operating profile still make this a reject. Current public signals conflict in places, so management confidence is medium rather than high.',
        'evidence_rows': [
            ev('1600-vine-1600-vine-st', 'amenities', 'Official marketing still shows extensive shared amenities, including reservable workspaces, rooftop terraces, and a 24-hour fitness center.', 'official', '1600 VINE amenities', 'https://www.1600vine.com/amenities', 'confirmed', 'positive', 'Amenities page highlights reservable workspaces, rooftop terraces, and a 24-hour fitness center with fiber Wi-Fi.'),
            ev('1600-vine-1600-vine-st', 'management', 'Sentral publicly announced that 1600 Vine joined its Los Angeles portfolio in July 2025.', 'news', 'Yahoo Finance / Sentral press release', 'https://finance.yahoo.com/news/sentral-expands-portfolio-los-angeles-115000377.html', 'confirmed', 'neutral', 'The July 10, 2025 press release says Sentral added 1600 Vine to its portfolio.'),
            ev('1600-vine-1600-vine-st', 'community_stability', 'Recent local coverage still describes 1600 Vine as a building built around content-creation spaces and influencer activity.', 'news', 'NBC Los Angeles', 'https://www.nbclosangeles.com/news/local/tiktok-ban-la-content-creators-1600-vine-hollywood/3394832/', 'confirmed', 'mixed', 'NBC describes creator-oriented “wedges” and the building as a place for influencers in Hollywood.'),
            ev('1600-vine-1600-vine-st', 'management', 'A public complaints index accessible on the web showed no closed complaints in the last three years, which partially conflicts with the repo’s legacy collapse note.', 'public_record', 'BCA complaint index', 'https://report.checkbca.org/1600-vine-at-hollywood-and-vine-100109774/complaints', 'confirmed', 'neutral', 'The BCA page reported 0 complaints closed in the last 3 years.'),
        ],
    },
    'columbia-square-living-1550-n-el-centro-ave': {
        'management_company': 'Greystar',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '4', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '4', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '5',
        'pricing_transparency_score': '4',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'medium',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Confirm whether the target unit faces away from adjacent construction and verify actual package handling, parking assignment, and approval speed. Confirm current parking operations, package handling, and any construction-exposed stacks.',
        'notes': 'Tour candidate remains justified. Current public review signals are strong, but the resident valet petition and the construction-adjacency note mean parking and exposure still need direct verification before lease-level commitment.',
        'evidence_rows': [
            ev('columbia-square-living-1550-n-el-centro-ave', 'amenities', 'The official site still markets Columbia Square Living as a modern high-amenity apartment community in Hollywood.', 'official', 'Columbia Square Living official site', 'https://www.columbiasquareliving.com/', 'confirmed', 'positive', 'Official site describes a modern apartment community with world-class amenities.'),
            ev('columbia-square-living-1550-n-el-centro-ave', 'management', 'Apartments.com currently shows a strong 4.8/5 rating across 13 reviews.', 'review', 'Apartments.com', 'https://www.apartments.com/columbia-square-living-los-angeles-ca/2v16sgc/', 'corroborated', 'positive', 'Apartments.com showed 4.8 stars from 13 reviews on March 22, 2026.'),
            ev('columbia-square-living-1550-n-el-centro-ave', 'pricing_transparency', 'Residents organized a public petition in 2024 asking management to reinstate valet service, indicating a real parking-operations friction point.', 'review', 'Change.org resident petition', 'https://www.change.org/p/reinstate-valet-service-at-columbia-square-living', 'anecdotal', 'negative', 'The petition says valet removal undermined a service residents considered part of the building’s value.'),
        ],
    },
    'modera-argyle-6220-selma-ave': {
        'management_company': 'Mill Creek Residential',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '2', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'unknown',
        'pricing_risk': 'medium',
        'status': 'rejected',
        'open_questions': '',
        'notes': 'Rejected, but with an explicit conflict note. Current public reviews are better than the repo’s earlier caution, yet the prior noise-enforcement concern plus aggressive concessioning and a nightlife-adjacent location still keep it below the line for this search.',
        'evidence_rows': [
            ev('modera-argyle-6220-selma-ave', 'location_fit', 'The official site emphasizes that the building sits one block off Sunset and close to theaters, live music, dining, and nightlife.', 'official', 'Modera Argyle official site', 'https://www.moderaargyle.com/', 'confirmed', 'mixed', 'Official copy stresses immediate proximity to Sunset and Hollywood nightlife.'),
            ev('modera-argyle-6220-selma-ave', 'management', 'Apartments.com currently shows 5.0/5 across 32 reviews, which conflicts with the repo’s older management caution.', 'review', 'Apartments.com', 'https://www.apartments.com/modera-argyle-los-angeles-ca/gfvt2ky/', 'corroborated', 'positive', 'Apartments.com showed 5.0 stars from 32 reviews on March 22, 2026.'),
            ev('modera-argyle-6220-selma-ave', 'pricing_transparency', 'Public listings were advertising unusually heavy concessions, including up to 10 weeks free, which signals lease-up pressure and requires careful fee review.', 'review', 'ApartmentHomeLiving.com', 'https://www.apartmenthomeliving.com/apartment-finder/Modera-Argyle-Los-Angeles-CA-90028-17944702', 'confirmed', 'mixed', 'The listing promoted up to 10 weeks free depending on lease term.'),
        ],
    },
    'ava-hollywood-la-pietra-6677-w-santa-monica-blvd': {
        'management_company': 'AvalonBay Communities',
        'quiet_score': '1', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '3', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '4',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'high',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'low',
        'status': 'rejected',
        'open_questions': '',
        'notes': 'Rejected because the repo’s older structural sound-transfer note is still decision-relevant and has not been affirmatively disproved by current public evidence. Current leasing pages look healthy, but they do not erase a previously confirmed floor/ceiling defect for a quiet-first search.',
        'evidence_rows': [
            ev('ava-hollywood-la-pietra-6677-w-santa-monica-blvd', 'amenities', 'The official Avalon page still markets a large amenity package, including chill spaces with Wi-Fi, a 5,000-square-foot fitness center, and a pool.', 'official', 'AvalonBay official site', 'https://www.avaloncommunities.com/california/los-angeles-apartments/ava-hollywood-at-la-pietra-place/', 'confirmed', 'positive', 'Official site highlights lounge seating with Wi-Fi, a 5,000 sq. ft. fitness center, and pool access.'),
            ev('ava-hollywood-la-pietra-6677-w-santa-monica-blvd', 'pricing_transparency', 'Current third-party listings still show large active inventory with clear published pricing and floor-plan ranges.', 'review', 'Zillow', 'https://www.zillow.com/apartments/los-angeles-ca/ava-hollywood-at-la-pietra-place/CjjCbw/', 'confirmed', 'positive', 'Zillow showed studio to larger homes with in-unit washer/dryer and current pricing on March 22, 2026.'),
            ev('ava-hollywood-la-pietra-6677-w-santa-monica-blvd', 'management', 'Apartment Finder still showed 16 ratings and reviews, so public resident signal exists even though the repo keeps a quiet-related hard stop.', 'review', 'Apartment Finder', 'https://www.apartmentfinder.com/California/Los-Angeles-Apartments/Ava-Hollywood-At-La-Pietra-Place-Apartments-rqlz090', 'corroborated', 'mixed', 'Apartment Finder listed 16 ratings and reviews in the current public profile.'),
        ],
    },
    'domain-west-hollywood-7141-santa-monica-blvd': {
        'management_company': 'Sares Regis',
        'quiet_score': '2', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '2', 'management_confidence': 'medium', 'management_evidence_count': '3',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'high',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'rejected',
        'open_questions': 'Confirm coworking or conference space and current fee disclosures.',
        'notes': 'Rejected with conflict documented. Current review-platform averages are not bad, but the repo history of structural noise, management churn, and move-in-readiness issues is still serious enough to keep this out of the tour set.',
        'evidence_rows': [
            ev('domain-west-hollywood-7141-santa-monica-blvd', 'amenities', 'The official site still markets a full luxury amenity stack with views, sky deck, and upscale shared spaces.', 'official', 'Domain WeHo official site', 'https://domainweho.com/', 'confirmed', 'positive', 'Official copy describes skyline views, a sky deck, and upscale community amenities in central West Hollywood.'),
            ev('domain-west-hollywood-7141-santa-monica-blvd', 'management', 'RealPage resident-review aggregation showed a 4.4/5 average across 276 reviews, which conflicts with the repo’s older management concern.', 'review', 'Modern Message / RealPage', 'https://modernmsg.com/domain-west-hollywood', 'corroborated', 'positive', 'Search results showed an average rating of 4.4 stars from 276 reviews.'),
            ev('domain-west-hollywood-7141-santa-monica-blvd', 'amenities', 'Apartments.com still lists in-unit laundry and current pricing, confirming that the building remains competitively merchandised.', 'review', 'Apartments.com', 'https://www.apartments.com/domain-weho-west-hollywood-ca/mkn8fgk/', 'confirmed', 'positive', 'Apartments.com showed current availability, pricing, and in-unit washer/dryer.'),
        ],
    },
    'the-baxter-1818-n-cherokee-ave': {
        'management_company': 'SD Property Management',
        'quiet_score': '3', 'quiet_confidence': 'low', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '3',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Because the building is new and review-light, verify noise transfer, package handling, exact unit readiness, concessions, and after-hours support in person. Confirm access control, package handling, and operating maturity under current team.',
        'notes': 'Still worth touring. The amenity package is unusually complete for the target, but nearly all uncertainty is maturity risk: the building is new enough that operating quality, noise transfer, and staff responsiveness still need onsite validation.',
        'evidence_rows': [
            ev('the-baxter-1818-n-cherokee-ave', 'amenities', 'The official site markets The Baxter as a new 86-unit luxury building with a rooftop deck, social lounge, and onsite parking.', 'official', 'The Baxter official site', 'https://thebaxterhollywood.com/?rcstdid=Mg%3D%3D-YRjTEizZPgM%3D', 'confirmed', 'positive', 'Official site describes a brand new 86-unit, 7-story building with rooftop deck, social lounge, and parking.'),
            ev('the-baxter-1818-n-cherokee-ave', 'amenities', 'Apartments.com lists secured parcel room, rooftop communal workspace, EV chargers, package service, and in-unit washer/dryer.', 'review', 'Apartments.com', 'https://www.apartments.com/the-baxter-los-angeles-ca/mtsg17j/', 'confirmed', 'positive', 'Current listing shows secured parcel room, rooftop working space, EV charging, and in-unit washer/dryer.'),
            ev('the-baxter-1818-n-cherokee-ave', 'management', 'Urbanize LA reported the project completed in 2024 with 86 units over a two-level garage, which reinforces the new-building context and thin operating history.', 'news', 'Urbanize LA', 'https://la.urbanize.city/post/rendering-vs-reality-baxter-hollywood-apartments-1818-n-cherokee-avenue', 'confirmed', 'neutral', 'Urbanize LA described a just-completed seven-story building with 86 units and a 61-car garage.'),
        ],
    },
    'sunset-vine-tower-1480-vine-st': {
        'management_company': 'SRG Residential',
        'quiet_score': '1', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '2', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '2', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '1',
        'location_fit_score': '3',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'medium',
        'pricing_risk': 'medium',
        'status': 'rejected',
        'open_questions': '',
        'notes': 'Rejected because the current official positioning still leans into the exact Sunset/Vine exposure that the repo had already flagged as too risky for a quiet-first move. Public review depth exists, but it does not override the legacy quiet and maintenance concerns.',
        'evidence_rows': [
            ev('sunset-vine-tower-1480-vine-st', 'location_fit', 'The official site still explicitly markets a Sunset Boulevard high-rise lifestyle at the Sunset/Vine crossroads.', 'official', 'Sunset Vine Tower official site', 'https://sunsetvinetower.com/', 'confirmed', 'mixed', 'Official copy describes a sky-high sanctuary right on Sunset Boulevard.'),
            ev('sunset-vine-tower-1480-vine-st', 'management', 'SRG Residential announced it had been awarded management of Sunset Vine Tower, confirming a recent management-side milestone.', 'news', 'Sares Regis Group news', 'https://www.sares-regis.com/post/srg-residential-awarded-management-of-high-rise-on-historic-sunset-vine', 'confirmed', 'neutral', 'SRG said it inked the management contract for Sunset Vine Tower.'),
            ev('sunset-vine-tower-1480-vine-st', 'management', 'Birdeye shows a meaningful body of public resident feedback, indicating that review depth exists even if the repo keeps a reject decision.', 'review', 'Birdeye', 'https://reviews.birdeye.com/sunset-vine-tower-apartments-156632004298060', 'corroborated', 'mixed', 'Birdeye showed 46 customer reviews in the public profile.'),
        ],
    },
    'zen-hollywood-1825-n-las-palmas-ave': {
        'management_company': 'Vista Associates, Inc.',
        'quiet_score': '1', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '2', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'high',
        'location_noise_risk': 'medium',
        'security_risk': 'high',
        'pricing_risk': 'medium',
        'status': 'rejected',
        'open_questions': 'Confirm whether any rooftop work or lounge area exists and clarify current valet versus self-parking operations.',
        'notes': 'Rejected because the repo’s quiet and security objections remain decisive for this search. Current public listings still show a rich amenity package, but they do not resolve the earlier balcony break-in pattern and structural sound-transfer concern.',
        'evidence_rows': [
            ev('zen-hollywood-1825-n-las-palmas-ave', 'amenities', 'The official site continues to market concierge service, business center, smart-home features, and valet parking.', 'official', 'ZEN Hollywood official site', 'https://www.zenhollywoodapts.com/', 'confirmed', 'positive', 'Official copy calls out 24-hour concierge service, business center, and valet parking.'),
            ev('zen-hollywood-1825-n-las-palmas-ave', 'amenities', 'Apartments.com currently lists package service, concierge, conference rooms, EV charging, and key-fob entry.', 'review', 'Apartments.com', 'https://www.apartments.com/zen-hollywood-los-angeles-ca/wr9hjth/', 'confirmed', 'positive', 'Current listing includes package service, concierge, conference rooms, EV charging, and key-fob entry.'),
            ev('zen-hollywood-1825-n-las-palmas-ave', 'management', 'A separate public travel/review page surfaced favorable commentary about security and maintenance, creating a direct conflict with the repo’s older security concern.', 'review', 'Wanderlog aggregation', 'https://wanderlog.com/place/details/4172114/zen-hollywood', 'anecdotal', 'positive', 'The page describes management and security personnel as exceptional, which conflicts with the repo’s prior reject note.'),
        ],
    },
    'skyview-sunset-1511-n-fairfax-ave': {
        'management_company': 'SRG Residential',
        'quiet_score': '3', 'quiet_confidence': 'low', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '1',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Verify whether there is a real gym, whether any units face Sunset/Fairfax noise, and whether hot tub is the only water amenity.',
        'notes': 'Research complete, but not yet advanced. The building checks several operational boxes on paper, yet review depth is effectively nonexistent and the Sunset/Fairfax location creates an obvious external-noise question.',
        'evidence_rows': [
            ev('skyview-sunset-1511-n-fairfax-ave', 'amenities', 'The official site notes digital package reception, gated access, EV charging, covered parking, and a rooftop sky deck with hot tub.', 'official', 'Skyview Sunset official site', 'https://www.skyviewsunset.com/', 'confirmed', 'positive', 'Current official materials support package reception, gated access, EV charging, covered parking, and rooftop sky-deck amenities.'),
            ev('skyview-sunset-1511-n-fairfax-ave', 'management', 'Apartments.com currently shows no renter reviews, leaving operating quality under-documented.', 'review', 'Apartments.com', 'https://www.apartments.com/skyview-sunset-los-angeles-ca/s011r94/', 'confirmed', 'neutral', 'The public profile stated there were no renter reviews yet.'),
        ],
    },
    '7950-west-sunset-7950-w-sunset-blvd': {
        'management_company': 'Legacy Partners',
        'quiet_score': '3', 'quiet_confidence': 'low', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '3',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Verify management company, exact fee stack, and whether any available units are exposed to Sunset noise.',
        'notes': 'Research complete but not promoted yet. Amenity fit is strong and management can now be tied to Legacy Partners, but the building is still directly on Sunset and public resident experience remains thin in the visible web evidence.',
        'evidence_rows': [
            ev('7950-west-sunset-7950-w-sunset-blvd', 'amenities', 'The official site still markets a high-amenity community with strong lifestyle positioning on Sunset.', 'official', '7950 West Sunset official site', 'https://7950westsunset.com/', 'confirmed', 'positive', 'Official copy describes luxury apartments with top-tier amenities on Sunset Boulevard.'),
            ev('7950-west-sunset-7950-w-sunset-blvd', 'amenities', 'Current third-party listings continue to show active inventory, in-unit laundry, and published rents.', 'review', 'Apartments.com', 'https://www.apartments.com/7950-west-sunset-los-angeles-ca/8h53150/', 'confirmed', 'positive', 'Apartments.com showed current availability and pricing from March 2026.'),
            ev('7950-west-sunset-7950-w-sunset-blvd', 'management', 'Architecture and development references tied the project to Legacy Partners.', 'news', 'TCA Architects project page', 'https://tca-arch.com/work/790-west-sunset/', 'confirmed', 'neutral', 'The TCA project page identifies Legacy Partners as the client for 7950 West Sunset.'),
        ],
    },
    'the-crown-8350-santa-monica-blvd': {
        'management_company': 'First Light Property Management',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '5',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Verify full pet fee schedule, package-room reality, and whether rooftop hot tub is the only water amenity.',
        'notes': 'Research complete. The location fit is excellent and the building looks workable on paper, but public resident sentiment is only middling and a few practical details still need direct confirmation.',
        'evidence_rows': [
            ev('the-crown-8350-santa-monica-blvd', 'amenities', 'The official site continues to market rooftop and fitness amenities in a central West Hollywood location.', 'official', 'The Crown official site', 'https://thecrownweho.com/', 'confirmed', 'positive', 'Official copy markets luxury living with studio, one-bedroom, and two-bedroom homes in West Hollywood.'),
            ev('the-crown-8350-santa-monica-blvd', 'amenities', 'Apartments.com currently lists controlled access, package service, roof terrace, on-site fitness, and in-home washer/dryer.', 'review', 'Apartments.com', 'https://www.apartments.com/crown-apartments-west-hollywood-ca/7p41k4z/', 'confirmed', 'positive', 'Current listing shows controlled access, package service, roof terrace, and in-home washer/dryer.'),
            ev('the-crown-8350-santa-monica-blvd', 'management', 'Birdeye showed a 3.4/5 profile across 14 reviews, which is usable but not pristine.', 'review', 'Birdeye', 'https://reviews.birdeye.com/the-crown-apartments-156783049108434', 'corroborated', 'mixed', 'Birdeye displayed 3.4 stars from 14 reviews.'),
        ],
    },
    'element-weho-1425-n-crescent-heights-blvd': {
        'management_company': 'Moss & Company',
        'quiet_score': '3', 'quiet_confidence': 'low', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '1',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '5',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Verify postal code, rooftop presence, and exact package-handling process after hours. Confirm EV charging and rooftop access or equivalent outdoor workspace amenity.',
        'notes': 'Research complete, but still evidence-thin. West Hollywood fit is strong and the essentials largely appear present, yet EV charging, rooftop utility, and after-hours package handling remain unresolved in visible public materials.',
        'evidence_rows': [
            ev('element-weho-1425-n-crescent-heights-blvd', 'amenities', 'Official materials and the repo note support package concierge, controlled access, pool, gym, garage parking, and pets welcome.', 'official', 'Element WeHo official site', 'https://www.elementweho.com/', 'confirmed', 'positive', 'Current official materials support package concierge, controlled access, pool, gym, garage parking, and pet-friendly terms.'),
            ev('element-weho-1425-n-crescent-heights-blvd', 'amenities', 'Apartments.com and Zillow both continue to show in-unit washer/dryer and active inventory.', 'review', 'Apartments.com', 'https://www.apartments.com/element-weho-west-hollywood-ca/wn8k8ek/', 'confirmed', 'positive', 'Third-party listings show active inventory and in-unit washer/dryer.'),
        ],
    },
    'aka-8500-sunset-8500-sunset-blvd': {
        'management_company': 'Korman Communities',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '4', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '2',
        'community_stability_score': '4', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '4',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Verify exact pet terms, whether there is any coworking-style work area, and which available units are least exposed to Sunset Strip noise.',
        'notes': 'Tour candidate. The building looks professionally run and very well equipped, with the main tradeoff being Sunset Strip exposure rather than missing essentials or weak operations.',
        'evidence_rows': [
            ev('aka-8500-sunset-8500-sunset-blvd', 'amenities', 'The official site still markets pet-friendly annual leasing with pool deck, high-tech fitness center, and 24/7 resident services for packages and deliveries.', 'official', 'Apartment Residences at AKA official site', 'https://www.8500sunsetapartments.com/', 'confirmed', 'positive', 'Official materials support pool deck, high-tech fitness center, and 24/7 resident services.'),
            ev('aka-8500-sunset-8500-sunset-blvd', 'amenities', 'Apartment Finder currently lists an outdoor lounge and pool deck, fitness center, private cinema, and a 24-hour on-site team.', 'review', 'Apartment Finder', 'https://www.apartmentfinder.com/California/West-Hollywood-Apartments/Aka-West-Hollywood-Apartment-Residences-Apartments-m5bpqmh', 'confirmed', 'positive', 'Public listing reinforces the outdoor lounge, pool deck, private cinema, and 24-hour team.'),
            ev('aka-8500-sunset-8500-sunset-blvd', 'pricing_transparency', 'Apartments.com still shows active inventory and current pricing for the building.', 'review', 'Apartments.com', 'https://www.apartments.com/aka-west-hollywood-apartment-residences-west-hollywood-ca/x4brlmm/', 'confirmed', 'positive', 'Apartments.com displayed current leasing inventory and pricing.'),
        ],
    },
    'silhouette-apartments-1233-n-highland-ave': {
        'management_company': 'Greystar',
        'quiet_score': '3', 'quiet_confidence': 'low', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Confirm package handling, parking, and whether current resident evidence remains thin.',
        'notes': 'Tour candidate with thin evidence. The building matches the target profile well on paper and current listings show real inventory, but it is still new enough that the review base is not yet deep.',
        'evidence_rows': [
            ev('silhouette-apartments-1233-n-highland-ave', 'amenities', 'Current listings continue to show central air conditioning, pet-friendly terms, and active inventory.', 'review', 'Zillow', 'https://www.zillow.com/apartments/los-angeles-ca/silhouette-apartments/CjHsns/', 'confirmed', 'positive', 'Zillow showed pet-friendly homes with central air conditioning and active inventory.'),
            ev('silhouette-apartments-1233-n-highland-ave', 'management', 'Apartments.com currently shows a 5.0/5 rating but only across 2 reviews, so the signal is positive but very shallow.', 'review', 'Apartments.com', 'https://www.apartments.com/silhouette-apartments-los-angeles-ca/7h539fy/', 'corroborated', 'positive', 'Apartments.com displayed 5.0 stars from 2 reviews.'),
            ev('silhouette-apartments-1233-n-highland-ave', 'amenities', 'RentCafe continues to show dozens of available one- and two-bedroom units, which confirms leasing activity and category fit.', 'review', 'RentCafe', 'https://www.rentcafe.com/apartments/ca/los-angeles/silhouette0/default.aspx', 'confirmed', 'positive', 'RentCafe showed 32 available units and secure online application flow.'),
        ],
    },
    'avalon-west-hollywood-7316-santa-monica-blvd': {
        'management_company': 'AvalonBay Communities',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '4', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '4', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '5',
        'pricing_transparency_score': '4',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'low',
        'status': 'tour_candidate',
        'open_questions': 'Confirm access control and package handling details, plus full recurring fee stack.',
        'notes': 'Tour candidate. The location fit is excellent, the operator is established, and the fee stack appears more transparent than many peers, with the main remaining questions centered on access control and package handling.',
        'evidence_rows': [
            ev('avalon-west-hollywood-7316-santa-monica-blvd', 'amenities', 'The official Avalon site still markets a broad unit mix and a professionally operated community in a prime West Hollywood location.', 'official', 'AvalonBay official site', 'https://www.avaloncommunities.com/california/west-hollywood-apartments/avalon-west-hollywood/', 'confirmed', 'positive', 'Official materials describe studios through townhomes and Signature Collection homes in West Hollywood.'),
            ev('avalon-west-hollywood-7316-santa-monica-blvd', 'amenities', 'Apartments.com currently lists washer/dryer in unit, on-site retail, pool, and fitness center.', 'review', 'Apartments.com', 'https://www.apartments.com/avalon-west-hollywood-west-hollywood-ca/wv7mqpk/', 'confirmed', 'positive', 'Current listing shows in-unit washer/dryer, on-site retail, pool, and fitness center.'),
            ev('avalon-west-hollywood-7316-santa-monica-blvd', 'management', 'Birdeye still shows a large body of public resident reviews for the property.', 'review', 'Birdeye', 'https://reviews.birdeye.com/avalon-west-hollywood-156632295346353', 'corroborated', 'positive', 'Birdeye showed 248 customer reviews in the current public profile.'),
        ],
    },
    'line-lofts-1737-n-las-palmas-ave': {
        'management_company': 'WSI Management, LLC',
        'quiet_score': '4', 'quiet_confidence': 'medium', 'quiet_evidence_count': '2',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '1',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Recheck 1BR availability, package handling, and parking details.',
        'notes': 'Research complete. The side-street location is a real positive for quiet risk, but the current public inventory looks studio-heavy and the building should not move further until one-bedroom availability is confirmed.',
        'evidence_rows': [
            ev('line-lofts-1737-n-las-palmas-ave', 'quiet', 'The official position is that the building sits on a quiet street just off Hollywood Boulevard.', 'official', 'Line Lofts official site', 'https://www.thelinelofts.com/', 'confirmed', 'positive', 'Current official materials emphasize a quiet street off Hollywood Boulevard.'),
            ev('line-lofts-1737-n-las-palmas-ave', 'amenities', 'Apartments.com currently shows only studio inventory, along with reduced rates and one-month-free offers.', 'review', 'Apartments.com', 'https://www.apartments.com/line-lofts-hollywood-ca/rspqcx2/', 'confirmed', 'mixed', 'Public listing showed studios only and current specials on March 22, 2026.'),
            ev('line-lofts-1737-n-las-palmas-ave', 'amenities', 'Zumper continues to show controlled access, on-site maintenance, on-site management, and gated covered parking.', 'review', 'Zumper', 'https://www.zumper.com/apartment-buildings/p182500/the-line-lofts-hollywood-hills-west-los-angeles-ca', 'confirmed', 'positive', 'Zumper highlights controlled access, on-site maintenance, on-site manager, and gated covered parking.'),
        ],
    },
    'the-charlie-weho-7617-santa-monica-blvd': {
        'management_company': 'Greystar',
        'quiet_score': '3', 'quiet_confidence': 'low', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'low', 'management_evidence_count': '1',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '2',
        'community_stability_score': '3', 'community_stability_confidence': 'low', 'community_stability_evidence_count': '1',
        'location_fit_score': '5',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'unknown',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Confirm access control, EV charging, package handling, and review depth as more residents move in.',
        'notes': 'Research complete but still too thin to advance. The location is attractive and the operator is known, but the visible review base is effectively zero and key operational details remain under-documented.',
        'evidence_rows': [
            ev('the-charlie-weho-7617-santa-monica-blvd', 'amenities', 'The official site continues to market a modern West Hollywood community close to dining and nightlife.', 'official', 'The Charlie WeHo official site', 'https://thecharlieweho.com/', 'confirmed', 'positive', 'Official copy markets modern West Hollywood living near dining and nightlife.'),
            ev('the-charlie-weho-7617-santa-monica-blvd', 'management', 'Apartments.com currently shows 0 reviews, which leaves resident-operations evidence very thin.', 'review', 'Apartments.com', 'https://www.apartments.com/the-charlie-weho-west-hollywood-ca/clgxc7f/', 'confirmed', 'neutral', 'The public profile showed 0 reviews.'),
            ev('the-charlie-weho-7617-santa-monica-blvd', 'pricing_transparency', 'Greystar’s current page confirms that homes are actively leasing under the operator’s platform.', 'official', 'Greystar property page', 'https://www.greystar.com/the-charlie-weho-west-hollywood-ca/p_20735', 'confirmed', 'positive', 'Greystar continues to list live availability and pricing.'),
        ],
    },
    'vantage-hollywood-1710-n-fuller-ave': {
        'management_company': 'Equity Residential',
        'quiet_score': '4', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '4', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '3',
        'community_stability_score': '4', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '4',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Verify in-unit washer and dryer at the specific unit level because the official site describes it as select-home.',
        'notes': 'Tour candidate. Vantage combines strong management depth with a quieter-feeling side-street address than many Hollywood options, but the select-home washer/dryer issue has to be unit-matched before anything moves forward.',
        'evidence_rows': [
            ev('vantage-hollywood-1710-n-fuller-ave', 'amenities', 'Official materials support controlled entry, Amazon Hub lockers, rooftop lounge, pool, 24-hour fitness, and EV charging.', 'official', 'Equity Apartments official site', 'https://www.equityapartments.com/los-angeles/west-hollywood/vantage-apartments', 'confirmed', 'positive', 'Current official materials support controlled entry, Amazon Hub lockers, rooftop lounge, pool, 24-hour fitness, and EV charging.'),
            ev('vantage-hollywood-1710-n-fuller-ave', 'management', 'Birdeye shows a large body of public resident reviews for the property.', 'review', 'Birdeye', 'https://reviews.birdeye.com/vantage-hollywood-apartments-156799630348894', 'corroborated', 'positive', 'Birdeye showed 235 customer reviews in the public profile.'),
            ev('vantage-hollywood-1710-n-fuller-ave', 'pricing_transparency', 'Zumper currently lists active pricing and a verified profile, which helps on rent visibility.', 'review', 'Zumper', 'https://www.zumper.com/apartment-buildings/p16283/vantage-hollywood-hollywood-hills-west-los-angeles-ca', 'confirmed', 'positive', 'Zumper showed verified listing status and live pricing for studios through 2BRs.'),
        ],
    },
    'hanover-hollywood-6200-w-sunset-blvd': {
        'management_company': 'Hanover Company',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '4', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '3',
        'community_stability_score': '3', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Resolve pet-policy conflict in writing and confirm any package-room or concierge setup.',
        'notes': 'Tour candidate. Hanover looks unusually strong on workspace and building operations, with the main issues being Sunset exposure and the need to pin down pet-policy details and package handling in writing.',
        'evidence_rows': [
            ev('hanover-hollywood-6200-w-sunset-blvd', 'amenities', 'The official site continues to market a brand-new luxury community steps from Hollywood & Vine.', 'official', 'Hanover Hollywood official site', 'https://www.hanoverhollywood.com/', 'confirmed', 'positive', 'Official copy describes a brand-new luxury community on Sunset Boulevard near Hollywood & Vine.'),
            ev('hanover-hollywood-6200-w-sunset-blvd', 'amenities', 'Apartments.com currently lists package service, controlled access, video patrol, study lounge, pool, and rooftop skydecks.', 'review', 'Apartments.com', 'https://www.apartments.com/hanover-hollywood-los-angeles-ca/9zcp565/', 'confirmed', 'positive', 'Current listing shows package service, controlled access, video patrol, study lounge, pool, and rooftop skydecks.'),
            ev('hanover-hollywood-6200-w-sunset-blvd', 'pricing_transparency', 'ApartmentHomeLiving continues to show active pricing and current inventory.', 'review', 'ApartmentHomeLiving.com', 'https://www.apartmenthomeliving.com/apartment-finder/Hanover-Hollywood-Los-Angeles-CA-90028-6188561', 'confirmed', 'positive', 'Public profile showed current pricing and availability.'),
        ],
    },
    'lumina-hollywood-1522-gordon-st': {
        'management_company': 'Morguard',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '3',
        'community_stability_score': '3', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '1',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'low',
        'pricing_risk': 'medium',
        'status': 'tour_candidate',
        'open_questions': 'Confirm EV charging, package handling, parking, and any formal coworking or meeting space.',
        'notes': 'Tour candidate with moderate confidence. Lumina looks operationally solid enough to keep alive, especially with concierge and controlled access, but some day-to-day logistics are still unclear and should be checked before touring priority rises further.',
        'evidence_rows': [
            ev('lumina-hollywood-1522-gordon-st', 'amenities', 'The official site continues to show active leasing for studio through two-bedroom homes.', 'official', 'Lumina Hollywood official site', 'https://luminahollywood.com/', 'confirmed', 'positive', 'Official materials show live inventory for studio, one-bedroom, and two-bedroom homes.'),
            ev('lumina-hollywood-1522-gordon-st', 'amenities', 'Apartments.com currently lists stacked washer/dryer, pool, fitness center, bicycle storage, and media room.', 'review', 'Apartments.com', 'https://www.apartments.com/lumina-hollywood-los-angeles-ca/nrmg09n/', 'confirmed', 'positive', 'Current listing shows stacked washer/dryer, pool, fitness center, bicycle storage, and media center.'),
            ev('lumina-hollywood-1522-gordon-st', 'management', 'The BBB profile currently shows an A+ business rating, although the building is not BBB accredited.', 'public_record', 'Better Business Bureau', 'https://www.bbb.org/us/ca/los-angeles/profile/not-elsewhere-classified/lumina-hollywood-apartments-1216-1000054409', 'confirmed', 'positive', 'BBB showed an A+ rating while also noting the property is not accredited.'),
        ],
    },
    'el-centro-apartments-and-bungalows-6200-hollywood-blvd': {
        'management_company': 'APT Residential',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '3', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '4', 'amenity_confidence': 'medium', 'amenity_evidence_count': '3',
        'community_stability_score': '3', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '3',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'medium',
        'security_risk': 'medium',
        'pricing_risk': 'medium',
        'status': 'research_complete',
        'open_questions': 'Confirm cat policy, EV charging, package handling, and the full monthly parking or amenity fee stack.',
        'notes': 'Research complete. El Centro is viable on paper and has meaningful public review depth, but it still needs fee-stack, cat-policy, and package-handling clarification before it should move into the active tour group.',
        'evidence_rows': [
            ev('el-centro-apartments-and-bungalows-6200-hollywood-blvd', 'amenities', 'The official site continues to market active leasing for the community in Hollywood.', 'official', 'El Centro official site', 'https://www.elcentrohollywood.com/', 'confirmed', 'positive', 'Official materials continue to advertise leasing and location advantages in Hollywood.'),
            ev('el-centro-apartments-and-bungalows-6200-hollywood-blvd', 'amenities', 'Apartments.com currently shows a 507-unit 2018 project with 12-24 month leases, active leasing, and a large shared amenity base.', 'review', 'Apartments.com', 'https://www.apartments.com/el-centro-apartments-and-bungalows-hollywood-ca/m5m52rl/', 'confirmed', 'positive', 'Current listing shows a 507-unit, six-story building with active leasing and multiple lease options.'),
            ev('el-centro-apartments-and-bungalows-6200-hollywood-blvd', 'management', 'Birdeye shows a substantial body of public resident reviews for the property.', 'review', 'Birdeye', 'https://reviews.birdeye.com/el-centro-apartments-bungalows-166314006829894', 'corroborated', 'mixed', 'Birdeye showed 183 customer reviews in the public profile.'),
        ],
    },
    'the-avenue-hollywood-1619-n-la-brea-ave': {
        'management_company': 'Greystar',
        'quiet_score': '3', 'quiet_confidence': 'medium', 'quiet_evidence_count': '1',
        'management_score': '4', 'management_confidence': 'medium', 'management_evidence_count': '2',
        'amenity_score': '5', 'amenity_confidence': 'high', 'amenity_evidence_count': '3',
        'community_stability_score': '4', 'community_stability_confidence': 'medium', 'community_stability_evidence_count': '2',
        'location_fit_score': '4',
        'pricing_transparency_score': '4',
        'approval_speed_business_days': '',
        'structural_noise_risk': 'unknown',
        'location_noise_risk': 'high',
        'security_risk': 'low',
        'pricing_risk': 'low',
        'status': 'tour_candidate',
        'open_questions': 'Confirm package handling and collect broader resident-operation signal beyond the currently visible public review set.',
        'notes': 'Tour candidate. The Avenue stands out for published total monthly pricing, strong amenities, and decent public review depth. The main issue is not missing functionality but exposure management on La Brea and making sure package operations are as good as the marketing.',
        'evidence_rows': [
            ev('the-avenue-hollywood-1619-n-la-brea-ave', 'pricing_transparency', 'The official site and current listings explicitly show total monthly price language and fee caveats rather than hiding all add-ons.', 'official', 'The Avenue official site', 'https://theavenuehollywood.com/', 'confirmed', 'positive', 'Official copy states additional fees may apply and points renters to lease documents before applying.'),
            ev('the-avenue-hollywood-1619-n-la-brea-ave', 'management', 'Apartments.com currently shows a 4.8/5 rating across 25 reviews and uses total monthly price display.', 'review', 'Apartments.com', 'https://www.apartments.com/the-avenue-hollywood-hollywood-ca/pzblp3t/', 'corroborated', 'positive', 'Apartments.com displayed 4.8 stars from 25 reviews and total monthly price visibility.'),
            ev('the-avenue-hollywood-1619-n-la-brea-ave', 'community_stability', 'Birdeye shows a meaningful body of public resident reviews for the property.', 'review', 'Birdeye', 'https://reviews.birdeye.com/the-avenue-hollywood-apartments-149468111686563', 'corroborated', 'positive', 'Birdeye showed 112 customer reviews in the public profile.'),
        ],
    },
}

# build default notes/open questions from source CSV for any fields not explicitly set


def md_packet(row, building_row, evidence_rows):
    lines = []
    lines.append(f"# {row['building_name']} building packet")
    lines.append('')
    lines.append('## Snapshot')
    lines.append(f"- Building ID: {row['building_id']}")
    lines.append(f"- Address: {row['address']}")
    primary_url = row['source_url'] or next((e['source_url'] for e in evidence_rows if e['source_type'] == 'official'), '')
    lines.append(f"- Primary URL: {primary_url}")
    lines.append(f"- Management company: {building_row['management_company']}")
    lines.append(f"- Recommended status: {building_row['status']}")
    lines.append(f"- Last updated: {building_row['last_updated']}")
    lines.append('')
    lines.append('## Scorecard')
    lines.append(f"- Quiet: {building_row['quiet_score']} ({building_row['quiet_confidence']}, evidence count {building_row['quiet_evidence_count']})")
    lines.append(f"- Management: {building_row['management_score']} ({building_row['management_confidence']}, evidence count {building_row['management_evidence_count']})")
    lines.append(f"- Amenity: {building_row['amenity_score']} ({building_row['amenity_confidence']}, evidence count {building_row['amenity_evidence_count']})")
    lines.append(f"- Community stability: {building_row['community_stability_score']} ({building_row['community_stability_confidence']}, evidence count {building_row['community_stability_evidence_count']})")
    lines.append(f"- Location fit: {building_row['location_fit_score']}")
    lines.append(f"- Pricing transparency: {building_row['pricing_transparency_score']}")
    lines.append('')
    lines.append('## Risks')
    lines.append(f"- Structural noise risk: {building_row['structural_noise_risk']}")
    lines.append(f"- Location noise risk: {building_row['location_noise_risk']}")
    lines.append(f"- Security risk: {building_row['security_risk']}")
    lines.append(f"- Pricing risk: {building_row['pricing_risk']}")
    lines.append('')
    lines.append('## Evidence summary')
    for e in evidence_rows:
        lines.append(f"- [{e['source_type']}] {e['claim']} Source: {e['source_name']} ({e['source_url']}). Note: {e['quote_or_note']}")
    lines.append('')
    lines.append('## Open questions')
    if building_row['open_questions']:
        for q in building_row['open_questions'].split(' | '):
            q = q.strip()
            if q:
                lines.append(f"- {q}")
    else:
        lines.append('- None beyond normal unit-level verification.')
    lines.append('')
    lines.append('## Notes')
    lines.append(building_row['notes'])
    return '\n'.join(lines)

all_packets = []

for bid, cfg_row in cfg.items():
    row = buildings[bid]
    building_row = {
        'building_id': bid,
        'management_company': cfg_row.get('management_company', row.get('management_company', '')),
        'quiet_score': cfg_row['quiet_score'],
        'quiet_confidence': cfg_row['quiet_confidence'],
        'quiet_evidence_count': cfg_row['quiet_evidence_count'],
        'management_score': cfg_row['management_score'],
        'management_confidence': cfg_row['management_confidence'],
        'management_evidence_count': cfg_row['management_evidence_count'],
        'amenity_score': cfg_row['amenity_score'],
        'amenity_confidence': cfg_row['amenity_confidence'],
        'amenity_evidence_count': cfg_row['amenity_evidence_count'],
        'community_stability_score': cfg_row['community_stability_score'],
        'community_stability_confidence': cfg_row['community_stability_confidence'],
        'community_stability_evidence_count': cfg_row['community_stability_evidence_count'],
        'location_fit_score': cfg_row['location_fit_score'],
        'pricing_transparency_score': cfg_row['pricing_transparency_score'],
        'approval_speed_business_days': cfg_row['approval_speed_business_days'],
        'structural_noise_risk': cfg_row['structural_noise_risk'],
        'location_noise_risk': cfg_row['location_noise_risk'],
        'security_risk': cfg_row['security_risk'],
        'pricing_risk': cfg_row['pricing_risk'],
        'status': cfg_row['status'],
        'review_scan_done': 'yes',
        'deep_research_done': 'yes',
        'open_questions': cfg_row.get('open_questions', row.get('open_questions', '')),
        'notes': cfg_row.get('notes', row.get('notes', '')),
        'last_updated': DATE,
    }
    packet = {
        'building_row': building_row,
        'evidence_rows': cfg_row['evidence_rows'],
        'packet_markdown': '',
    }
    packet['packet_markdown'] = md_packet(row, building_row, cfg_row['evidence_rows'])
    all_packets.append(packet)
    out_path = OUT / f"{bid}.json"
    with open(out_path, 'w') as f:
        json.dump(packet, f, indent=2)

with open(OUT / 'all_building_packets.jsonl', 'w') as f:
    for packet in all_packets:
        f.write(json.dumps(packet))
        f.write('\n')

# also create a simple index markdown
with open(OUT / 'INDEX.md', 'w') as f:
    f.write('# Building packet index\n\n')
    for packet in all_packets:
        br = packet['building_row']
        f.write(f"- {br['building_id']}: {br['status']}\n")
