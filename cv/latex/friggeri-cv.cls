\ProvidesClass{friggeri-cv}[2012/04/30 CV class]
\NeedsTeXFormat{LaTeX2e}

\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions\relax
\LoadClass{article}

%%%%%%%%%%
% Colors %
%%%%%%%%%%

\RequirePackage{xcolor}

\definecolor{white}{RGB}{255,255,255}

\definecolor{darkgray}{HTML}{333333}
\definecolor{gray}{HTML}{4D4D4D}
\definecolor{lightgray}{HTML}{999999}

\definecolor{green}{HTML}{35C26A}
\definecolor{orange}{HTML}{FDA333}
\definecolor{purple}{HTML}{8E44AD}
\definecolor{red}{HTML}{ff4d4d}
\definecolor{cyan}{HTML}{46B9DB}
\definecolor{maroon}{HTML}{800000}
\definecolor{blue}{HTML}{1E6291}
\definecolor{yellow}{HTML}{FFC300}
\definecolor{darkgray}{HTML}{4D4D4D}
\definecolor{orange}{HTML}{FDA333}
\definecolor{green}{HTML}{35C26A}
\definecolor{red}{HTML}{ff4d4d}

\ifdefined\@cv@print
  \colorlet{green}{gray}
  \colorlet{orange}{gray}
  \colorlet{purple}{gray}
  \colorlet{red}{gray}
  \colorlet{cyan}{gray}
  \colorlet{maroon}{gray}
  \colorlet{cyan}{gray}
  \colorlet{blue}{gray}
  \colorlet{orange}{gray}
  \colorlet{fillheader}{white}
  \colorlet{header}{gray}
\else
  \colorlet{fillheader}{gray}
  \colorlet{header}{white}
\fi
\colorlet{textcolor}{gray}
\colorlet{headercolor}{gray}

%%%%%%%%%
% Fonts %
%%%%%%%%%

\RequirePackage[quiet]{fontspec}
\RequirePackage{unicode-math}
 
\newfontfamily\bodyfont[]{Helvetica Neue}
\newfontfamily\thinfont[]{Helvetica Neue UltraLight}
\newfontfamily\headingfont[]{Helvetica Neue Condensed Bold}
 
\defaultfontfeatures{Mapping=tex-text}
\setmainfont[Mapping=tex-text, Color=textcolor]{Helvetica Neue Light}
 
%\setmathfont{XITS Math}

%%% modified by Karol Kozioł for ShareLaTex use
\RequirePackage[quiet]{fontspec}
\RequirePackage{unicode-math}

%\newfontfamily\bodyfont
%[BoldFont=texgyreheros-bold.otf,
%ItalicFont=texgyreheros-italic.otf,
%BoldItalicFont=texgyreheros-bolditalic.otf]
%{texgyreheros-regular.otf}
%\newfontfamily\thinfont[]{Lato-Light.ttf}
%\newfontfamily\headingfont[]{texgyreheros-bold.otf}

\defaultfontfeatures{Mapping=tex-text}
\setmainfont
[Mapping=tex-text, Color=textcolor,
BoldFont=texgyreheros-bold.otf,
ItalicFont=texgyreheros-italic.otf,
BoldItalicFont=texgyreheros-bolditalic.otf
]
{texgyreheros-regular.otf}

\setmathfont{texgyreheros-regular.otf}
%%%

%%%%%%%%%%
% Header %
%%%%%%%%%%

\RequirePackage{tikz}

\newcommand{\header}[5]{% <-- Accepts 5 arguments
  \begin{tikzpicture}[remember picture,overlay]
    % Background box for the header
    \node [rectangle, fill=fillheader, anchor=north, minimum width=\paperwidth, minimum height=4.5cm] (box) at (current page.north){};

    % Node 1: Name and Surname (Centered horizontally)
    \node [anchor=north] (name) at ([yshift=-1cm] box.north) {%
      \fontsize{40pt}{72pt}\color{header}%
      {\thinfont #1}{\bodyfont #2}%
    };

    % Node 2: Main Placement (e.g., Job Title) (Below Name)
    \node [anchor=north] at ([yshift=0cm] name.south) {%
      \fontsize{14pt}{24pt}\color{header}%
      \thinfont #3%
    };

    % Node 3: Additional Details (e.g., ISO Committee Member) (Below Main Placement)
    \node [anchor=north] at ([yshift=-0.7cm] name.south) {%
      \fontsize{12pt}{20pt}\color{header}%
      \thinfont #4%
    };

    % Node 4: Communication (e.g., Email) (Centered at the bottom of the header box)
    \node [anchor=north] at ([yshift=-3.8cm] box.north) {%
      \fontsize{12pt}{20pt}\color{header}%
	  \thinfont {\Letter\hspace{0.2em} #5} % Adds email icon and spacing
    };
  \end{tikzpicture}
  \vspace{2.8cm} % Reduced spacing to bring content closer
  \vspace{-2\parskip} % Adjust further as needed
}



%%%%%%%%%%%%%
% Structure %
%%%%%%%%%%%%%
\RequirePackage{parskip}

\newcounter{colorCounter}
\def\@sectioncolor#1#2#3#4#5{%
  {%
    \color{%
      \ifcase\value{colorCounter}%
        headercolor\or%
        headercolor\or%
        headercolor\or%
        headercolor\or%
        headercolor\or%
        headercolor\or%
        headercolor\or%
        headercolor\or%
        headercolor\else%
        headercolor\fi%
    } #1#2#3#4#5%
  }%
  \stepcounter{colorCounter}%
}

\renewcommand{\section}[1]{
  \par\vspace{\parskip}
  {%
    \LARGE\headingfont\color{headercolor}%
    \@sectioncolor #1%
  }
  \par\vspace{\parskip}
}

\renewcommand{\subsection}[1]{
  \par\vspace{.5\parskip}%
  {%
  \large\headingfont\color{headercolor} #1%
  }
  \par\vspace{.25\parskip}%
}

\newcommand{\specialsection}[1]{
  \par\vspace{\parskip}
  \hspace*{-3cm} % Move to the left by 5cm
  {%
    \LARGE\headingfont\color{headercolor}%
    \@sectioncolor #1%
  }
  \par\vspace{\parskip}
}

\pagestyle{empty}

%%%%%%%%%%%%%%%%%%%%
% List environment %
%%%%%%%%%%%%%%%%%%%%

\setlength{\tabcolsep}{0pt}
\newenvironment{entrylist}{%
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
}{%
  \end{tabular*}
}
\renewcommand{\bfseries}{\headingfont\color{headercolor}}
\newcommand{\entry}[4]{%
  #1&\parbox[t]{13cm}{%
    \textbf{#2}%
    \hfill%
    {\small\addfontfeature{Color=blue} #3}\\%
    #4\vspace{\parsep}%
  }\\}


%%%%%%%%%%%%%%%%%%%%%%
% List environment 2 %
%%%%%%%%%%%%%%%%%%%%%%

\setlength{\tabcolsep}{0pt}
\newenvironment{entrylist2}{%
  % Adjust the left margin by shifting the table 2 cm to the left
  \hspace*{-2.5cm}\begin{tabular*}{\dimexpr\textwidth+1cm\relax}{@{\extracolsep{\fill}}ll} 
}{%
  \end{tabular*}
}
\renewcommand{\bfseries}{\headingfont\color{headercolor}}
\newcommand{\entrytwo}[4]{% Renamed to \entrytwo to avoid conflict
  #1&\parbox[t]{14cm}{%
    \textbf{#2}%
    \hfill%
    {\small\addfontfeature{Color=blue} #3}\\%
    #4\vspace{\parsep}%
  }\\}


  
%%%%%%%%%%%%%%
% Side block %
%%%%%%%%%%%%%%

\RequirePackage[absolute,overlay]{textpos}
\setlength{\TPHorizModule}{0.8cm}
\setlength{\TPVertModule}{0.9cm}
\newenvironment{aside}
{
	\let\oldsection\section
	\renewcommand{\section}[1]
	{\par\vspace{\baselineskip}{\Large\headingfont\color{headercolor} ##1}}
	% Adjust the vertical position (4.33) to align with the "about me" title
    \begin{textblock}{4.5}(1.2, 5)
	\begin{flushright}
    \obeycr
}
{
	\restorecr\end{flushright}
	\end{textblock}
	\let\section\oldsection
}


%%%%%%%%%%%%%%%%
% Other tweaks %
%%%%%%%%%%%%%%%%

\RequirePackage[left=5cm,top=2cm,right=1.5cm,bottom=2cm,nohead,nofoot]{geometry}
\RequirePackage{hyperref}