%{
    #include "y.tab.h"
%}

%% 

"a"         { return ARTICLE; }
"the"       { return ARTICLE; }
"boy"       { return NOUN; }
"girl"      { return NOUN; }
"flower"    { return NOUN; }
"touches"   { return VERB; }
"likes"     { return VERB; }
"with"      { return PREPOSITION; }
"sees"      { return VERB; }
.           { /* ignore other characters */ }
""         {   /* ignore spaces */}

%%