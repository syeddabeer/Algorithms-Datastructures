# /***
# moving specific marked train cars identified by letters from different tracks to another in multiples of three, while also moving the ones that weren't marked out of the way.
# ***/

// ── Exact same logic as Python min_moves_multi ────────────────────
function minMovesMulti(track, markedCars, groupSize = 3) {
    const markedSet = new Set(markedCars);
    const results   = {};

    for (const carType of markedSet) {
        const positions = track
            .map((c, i) => c === carType ? i : -1)
            .filter(i => i !== -1);

        let moves = 0;

        for (let g = 0; g < positions.length; g += groupSize) {
            const group = positions.slice(g, g + groupSize);
            if (group.length < groupSize) break;

            const first    = group[0];
            const last     = group[group.length - 1];
            const span     = track.slice(first, last + 1);
            const blockers = span.filter(c => c !== carType).length;

            moves += blockers;
        }

        results[carType] = moves;
    }

    const total = Object.values(results).reduce((s, m) => s + m, 0);
    return { total, results };
}


// ── NEW: multi-track — just loops over tracks ─────────────────────
function minMovesMultiTrack(tracks, markedCars, groupSize = 3) {
    const allResults = {};
    let grandTotal   = 0;

    for (const [trackName, track] of Object.entries(tracks)) {
        const { total, results } = minMovesMulti(track, markedCars, groupSize);
        allResults[trackName]    = results;
        grandTotal              += total;
    }

    return { grandTotal, allResults };
}


// ── Example ───────────────────────────────────────────────────────
const tracks = {
    A : ['A','T','X','B','T','X','T','Z','C','X'],
    B : ['T','Z','T','D','T','Z','E','Z','X','T'],
    C : ['X','X','A','X','T','Z','T','Z','T','Z'],
};
const markedCars = ['T', 'X', 'Z'];

const { grandTotal, allResults } = minMovesMultiTrack(tracks, markedCars);

console.log(`Grand total moves: ${grandTotal}`);
for (const [trackName, results] of Object.entries(allResults)) {
    const trackTotal = Object.values(results).reduce((s, m) => s + m, 0);
    console.log(`\n  Track ${trackName} (${trackTotal} moves):`);
    for (const [carType, moves] of Object.entries(results)) {
        console.log(`    ${carType} → ${moves} move(s)`);
    }
}